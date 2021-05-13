n,h,w =list(map(int,input().split()))
ans=0
for _ in range(n):
    a1,b1=list(map(int,input().split()))
    if a1>=h and b1>=w:
        ans+=1
print(ans)
