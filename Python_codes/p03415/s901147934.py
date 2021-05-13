ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

s = []
for i in range(3):
  s.append(input())

for i in range(3):
  print(s[i][i],end="")
