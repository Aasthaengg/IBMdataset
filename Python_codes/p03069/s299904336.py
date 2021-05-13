n=int(input())
s=input()
countwhite=[0]*(n+1)
for i in range(n):
    if s[i]==".":
        countwhite[i+1]=countwhite[i]+1
    else:
        countwhite[i+1]=countwhite[i]
ans=10**8
for i in range(n+1):
    change=i-countwhite[i]+(countwhite[-1]-countwhite[i])
    ans=min(ans,change)
print(ans)