n,x=map(int,input().split())
m=[]
kai=n
for i in range(n):
  m.append(int(input()))
m.sort()
x=x-sum(m)
while x:
  if x >= m[0]:
    x=x-m[0]
    kai+=1
  else:
    break
print(kai)