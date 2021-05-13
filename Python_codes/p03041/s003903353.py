n,k=map(int,input().split())
s=input()
ans=""
for i in range(n):
    if i!=k-1:
        ans+=s[i]
    else:
        ans+=s[i].lower()
print(ans)