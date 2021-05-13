n,k=map(int,input().split())
ans=k
if n==1:
    print(k)
    exit()
for i in range(n-1):
    ans*=k-1
print(ans)