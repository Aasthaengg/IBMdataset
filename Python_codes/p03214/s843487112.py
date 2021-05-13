n=int(input())
a=list(map(int,input().split()))
m=sum(a)/n
for i in range(n):
  if i == 0:
    index=0
    d=abs(m-a[0])
  else:
    d_new = abs(m-a[i])
    if d_new < d:
      d = d_new
      index=i
print(index)