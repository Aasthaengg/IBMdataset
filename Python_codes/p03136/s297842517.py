n = int(input())
a = list(map(int, input().split()))
b = [0]*n
b = sorted(a)
c = 0
for i in range(n-1):
  c += b[i]
if c>b[n-1]:
  print("Yes")
else:
  print("No")