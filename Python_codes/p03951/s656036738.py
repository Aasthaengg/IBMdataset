N=int(input())
s=input()
t=input()
ans=10**9
for i in range(N+1):
    for j in range(N+1):
        u=s[:i]+t[j:]
        if len(u)<N:
            continue
        if u[:N]==s and u[-N:]==t:
            ans=min(ans,len(u))
print(ans)