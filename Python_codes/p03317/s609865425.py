n, k = map(int, input().split())
As = list(map(int, input().split()))
a=n-1
b=k-1
if a % b == 0:
  print(a//b)
else:
  print((a//b) + 1)