N, T = map(int, input().split())
t = list(map(int, input().split()))
t.append(t[-1]+T)

ans = 0
start = 0
stop = 0
for ti in t:
  if ti >= stop:
    ans += stop - start
    start = ti
  stop = ti+T
print(ans)