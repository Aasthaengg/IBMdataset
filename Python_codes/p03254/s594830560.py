N, x = map(int,input().split())
A = sorted([a for a in map(int,input().split())])

ans = 0

for a in A:
    x -= a
    ans += 1
    if x < 0:
        ans -= 1
        break
if x > 0:
    ans -= 1
print(ans)
