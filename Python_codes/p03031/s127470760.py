l = lambda: list(map(int, input().split()))
N,M = l()
K = [l() for _ in range(M)]
P = l()

ans = 0
fmt = "{:0" + str(N) + "b}"
for i in range(2**N):
    valid = True
    d = list(map(int, list(fmt.format(i))))
    for j in range(M):
        if not P[j] == sum([d[k - 1] for k in K[j][1:]]) % 2:
            valid = False
            break
    if valid:
        ans += 1

print(ans)