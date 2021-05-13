n=int(input())
k=int(input())

tmp=1
for _ in range(n):
  x=tmp*2
  y=tmp+k
  tmp=min(x,y)
  
print(tmp)