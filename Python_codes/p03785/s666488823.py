N,C,K = [int(hoge) for hoge in input().split()]
ans = 0
time = -float("inf")
bus = 0
Ts = sorted([int(input()) for i in range(N)])
for T in Ts:
    if (T > time + K) or bus==C:
        ans += 1
        time = T
        bus = 1
    else:
        bus += 1
print(ans)