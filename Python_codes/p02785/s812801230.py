n, k = map(int, input().split())
H = [int(i) for i in input().split()]

if len(H) <= k:
    ans = 0
else:
    H.sort()
    r = H
    if k != 0:
        r = H[:-k]
    ans = sum(r)

print(ans)