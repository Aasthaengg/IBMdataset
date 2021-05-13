n=int(input())
a=[]
for i in range(n):
  a.append(int(input()))
b=sorted(a,reverse=True)

c=a.index(b[0])
d=b.index(b[1])
for i in range(n):
  if i==c:
    print(b[1])
  else:
    print(b[0])
    
  
