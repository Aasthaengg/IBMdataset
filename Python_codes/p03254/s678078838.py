n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
ans = 0
for i in a:
    x -= i
    if x < 0: break
    else: ans += 1
if ans == n and x != 0: print(ans-1)
else: print(ans)
