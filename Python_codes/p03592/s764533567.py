N, M, K = map(int, input().split())
ok = False
for i in range(N + 1):
    for j in range(M + 1):
        now = M * i
        now -= j * i
        now += j * (N - i)
        if now == K:
            ok = True
if ok:
    print("Yes")
else:
    print("No")