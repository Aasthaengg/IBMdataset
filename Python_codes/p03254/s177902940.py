N, x, *A = map(int, open(0).read().split())
A.sort()
ans = 0
for a in A[:-1]:
    if x - a >= 0:
        x -= a
        ans += 1
    else:
        break
if x == A[-1]:
    ans += 1
print(ans)
