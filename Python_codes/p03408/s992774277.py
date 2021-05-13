n=int(input())
s=[input() for _ in range(n)]
m=int(input())
t=[input() for _ in range(m)]
ans=0
for i in set(s):
  tmp_pnt = s.count(i) - t.count(i)
  if tmp_pnt>ans:
    ans=tmp_pnt 
print(ans)