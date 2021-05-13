R, G, B, N = map(int, input().split())

lst = [R, G, B]
lst.sort()
k2, k1, k0 = lst

ans = 0
if lst != [1, 1, 1]:
    for n0 in range(N//k0 + 1):
        for n1 in range(N//k1 + 1):
            nn = (N - n0 * k0 - n1 * k1)
            if nn >= 0 and nn % k2 == 0: ans += 1
    print(ans)
else:
    for n0 in range(N+1):
        for n1 in range(n0, N+1):
            if n0 + n1 > N:continue
            if n0 == n1: ans += 1
            else: ans += 2
    print(ans)