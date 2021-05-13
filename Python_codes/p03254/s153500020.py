n, x = map(int, input().split())
a = map(int, input().split())
sa = sorted(a)
ans = 0
for q in sa:
    if x < 0:
        break
    x -= q
    ans += 1
print(ans - (0 if x == 0 else 1))
