n=int(input())
a=list(map(int,input().split()))

c=0

for i in range(n):
  d=0
  while d==0:
    if a[i]%2==0:
      a[i]//=2
      c+=1
    else:
      d=1
print(c)