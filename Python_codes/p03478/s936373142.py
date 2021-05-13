N, A, B = map(int, input().split())
l = list(range(1, N+1))
s = 0
for i in l:
  t = sum(map(int, list(str(i))))
  if A <= t <= B:
    s += i

print(s)