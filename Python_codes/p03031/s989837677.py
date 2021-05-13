N, M = map(int, input().split())

s_list = []
for i in range(M):
    s_list.append(list(map(int, input().split())))
P_list = list(map(int, input().split()))

ans = 0
for i in range(1 << N):
    S = ["OFF" for _ in range(N)]
    for j in range(N):
        if (i >> j) & 1 == 1:
            S[j] = "ON"
    m = 0
    while True:
        cnt = 0
        for s in range(1, len(s_list[m])):
            if S[s_list[m][s]-1] == "ON":
                cnt += 1
        if cnt % 2 != P_list[m]:
            break
        m += 1
        if m == M:
            break
    if m == M:
        ans += 1
print(ans)
