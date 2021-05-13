n,k=map(int,input().split())
s=input()
ans=""
for i in range(n):
    a=s[i]
    if i+1==k:
        a=a.swapcase()
    ans+=a
print(ans)
