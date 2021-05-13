h,w = map(int,input().split())
a = []
for i in range(h):
    a.append(list(map(int,input().split())))

ni=0
nj=0
st=0
sw=0
lis = []
while (True):
    #print(ni,nj)
    tmp =[]
    if a[ni][nj]%2==1:
        st=1
        tmp.extend([ni+1,nj+1])
    if sw==0 and nj<w-1:
        nj+=1
    elif sw==1 and nj>0:
        nj-=1
    elif nj==w-1 or nj==0:
        ni+=1
        sw=1-sw
    #print(ni,nj)
    if ni>h-1:
        break
    if st==1:
        a[ni][nj]+=1
        tmp.extend([ni+1,nj+1])
        lis.append(tmp)
    st=0
print(len(lis))
for i in range(len(lis)):
    print(*lis[i])
