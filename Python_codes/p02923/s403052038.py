n=int(input())
if n==1:
    print(0)
    exit()
h=list(map(int,input().split()))
height=h[0]
l=[]
cnt=0
for i in range(1,n):
    if h[i]<=height:
        cnt+=1
    else:
        cnt=0
    height=h[i]
    l.append(cnt)
print(max(l))