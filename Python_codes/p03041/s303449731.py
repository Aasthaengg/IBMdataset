n,k=map(int,input().split())
s=str(input())
ans=""
for i in range(n):
    if i==k-1:
        ans+=s[k-1].lower()
    else:
        ans+=s[i]

print(ans)