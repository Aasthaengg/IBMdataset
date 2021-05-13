n=int(input())
a=list(map(int,input().split()))
d=1
for i in range(n):
  if a[i]%2==1:
    d*=1
  else:
    d*=2
print(3**n-d)