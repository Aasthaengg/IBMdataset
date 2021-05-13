X, N = map(int,input().split())
P = list(map(int, input().split()))
forbid = set(P)

l, r = X, X
ans = float("inf")
while True:
    if l not in forbid:
        ans = l
        break
    if r not in forbid:
        ans = r
        break
    l -= 1
    r += 1

print(ans)
