n=int(input())
a=[]
e=1
for i in range(n):
  a.append(int(input()))
a.sort()
s=a.pop(0)
while a:
  k=a.pop(0)
  if s < k:
    e+=1
    s=k
print(e)