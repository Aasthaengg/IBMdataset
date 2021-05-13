#区間スケジューリング
n, m = map(int, input().split())
lst = []
for _ in range(m):
    a, b = map(int, input().split())
    lst.append([a, b])

lst.sort(key=lambda x:x[1])

ans = 0
ed = 0
for _ in lst:
    if _[0] < ed:
      pass
    else:
        ed = _[1]
        ans += 1
print(ans)
