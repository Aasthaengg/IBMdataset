n = int(input())
a = list(map(int,input().split()))
a.sort()
x =(a[0]+a[1])/2
if n > 2:
  for i in range(n-2):
    x = (x + a[i+2])/2
print(x)