n = int(input())
a = int((-0.5+(0.5**2+2*(n-1))**0.5)+1)
for i in range(a,0,-1):
  if n >= i:
    n-=i
    print(i)