n = int(input())
s = 0
for i in range(n):
  l = list(map(int, input().split()))
  s += (l[1] - l[0] + 1)
print(s)