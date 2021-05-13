n=int(input())
s=[input() for i in range(n)]
m=int(input())
t=[input() for i in range(m)]
ans=0
for i in range(n):
  a=s.count(s[i])-t.count(s[i])
  ans=max(ans,a)
print(ans)