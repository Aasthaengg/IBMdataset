k=int(input())
n=min(k+2,50)
a=list(range(n))
for i in range(n):
  a[i]+=k//n
for i in range(k%n):
  a[i]+=n
  for j in range(n):
    if i==j:continue
    a[j]-=1
print(n)
print(*a)