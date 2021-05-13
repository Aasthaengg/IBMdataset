n=int(input())
s=list(input())
l=[[0,s.count('.')]]
for i in range(n):
    if s[i]=='.':
        l.append([l[-1][0],l[-1][1]-1])
    else:
        l.append([l[-1][0]+1,l[-1][1]])

ans=10**10
for i in range(n+1):
    ans=min(ans,sum(l[i]))

print(ans)