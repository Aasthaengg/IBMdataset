n = int(input())
a = 0
for i in map(int, input().split()):
  a = a + i
if a % 2 == 0:
  print("YES")
else:
  print("NO")