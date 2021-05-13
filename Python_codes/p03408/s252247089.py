n=int(input())
s=[input() for i in range(n)]
m=int(input())
t=[input() for i in range(m)]

ans=0
cnt=0
for i in range(n):
  for j in range(n):
    if s[i]==s[j]:
      cnt+=1
  for k in range(m):
    if s[i]==t[k]:
      cnt-=1
  ans=max(ans,cnt)
  cnt=0
print(ans)