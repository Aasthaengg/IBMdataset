n = int(input())
t = list(map(int, input().split()))
s = sum(t)
m = int(input())
for _ in range(m):
  p, v = list(map(int, input().split()))
  print(s - t[p-1] + v)