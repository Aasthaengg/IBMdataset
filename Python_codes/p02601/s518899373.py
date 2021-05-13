a, b, c = map(int, input().split())
ans = False
k = int(input())

for i in range(k):
  if a < b * 2 ** i < c * 2 ** (k - i):
    ans = True

if ans == True:
  print("Yes")
else:
  print("No")