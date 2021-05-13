k, s = map(int, input().split())

if k > s:
    k = s

ans = 0
for x in range(k+1):
    rem = s - x
    if rem > 2 * k:
        continue
    elif rem > k:
        ans += 2 * k - rem + 1
    else:
        ans += rem + 1

print(ans)