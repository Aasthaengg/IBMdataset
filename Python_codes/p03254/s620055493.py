N, x = map(int, input().split())
A = sorted(list(map(int, input().split())))
res = 0
for a in A:
    x -= a
    res += 1
    if x < 0:
        x = abs(x)
        break
    elif x == 0:
        break

print(max(res-1, 0) if x>0 else res)
