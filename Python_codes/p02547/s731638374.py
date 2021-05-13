n = int(input())
a = [[int(i) for i in input().split()] for j in range(n)]
good = False
for i in range(n-2):
  ok = True
  for j in range(i, i+3):
    ok &= a[j][0] == a[j][1]
  good |= ok
print("Yes" if good else "No")