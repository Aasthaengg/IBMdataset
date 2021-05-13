n, x = map(int, input().split())
a_l = list(map(int, input().split()))
a_l = sorted(a_l)
ans = 0
for a in a_l:
    x = x-a
    if x < 0:
        break
    ans += 1
if x > 0:
    ans -= 1
print(ans)