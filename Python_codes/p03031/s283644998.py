N, M = map(int, input().split())
K = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))

ans = 0
# pow(2,N)のbit全探索
for num in range(1 << N):
    # 全ての電灯を確認
    # print(num)
    flag = True
    for m in range(M):
        count_m = 0
        for j in K[m][1:]:
            if num & (1 << (j - 1)):
                count_m += 1
        # print(m, count_m, K[m], P[m])
        if count_m % 2 != P[m]:
            flag = False
            break
    # print(num, flag)
    if flag:
        ans += 1

print(ans)