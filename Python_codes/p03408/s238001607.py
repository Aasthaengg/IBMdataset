from collections import defaultdict


n=int(input())
s=[input() for i in range(n)]
m=int(input())
t=[input() for i in range(m)]


dic=defaultdict(int)
for i in range(n):
    dic[s[i]]+=1

for i in range(m):
    dic[t[i]]-=1

ans=0
for i in dic.values():
    ans=max(ans,i)
print(ans)