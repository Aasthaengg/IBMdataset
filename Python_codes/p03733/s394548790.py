n, t = map(int, input().split())
T = list(map(int, input().split())) + [10 ** 19]

ans = 0
for t1, t2 in zip(T, T[1::]):
  if t2 - t1 < t:
    ans += t2 - t1
  else:
    ans += t
  
print(ans)
