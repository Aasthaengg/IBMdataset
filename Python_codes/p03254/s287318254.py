n,x=map(int,input().split())
a=sorted(list(map(int,input().split())))

cnt=0
for i in range(n):
    if x>0:
        x-=a[i]
        cnt+=1
        
if x>0:
    cnt-=1
if x<0:
    cnt-=1
print(cnt)
