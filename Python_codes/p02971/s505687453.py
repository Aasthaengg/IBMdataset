n=int(input())
a=[]
for i in range(n):
  a.append(int(input()))
b=sorted(a,reverse=True)
a1=b[0]
a2=b[1]
m=a.index(a1)
for i in range(n):
  if i==m:
    print(a2)
  else:
    print(a1)