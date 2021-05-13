n=int(input())
s=set()
for i in range(1,n):
  j=n-i
  if i==j:continue
  t=[i,j]
  t.sort()
  key=str(t[0])+str([1])
  s.add(key)
print(len(s))
