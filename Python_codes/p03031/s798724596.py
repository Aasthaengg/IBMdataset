N, M = map(int, input().split())
k, s = [[] for _ in range(2)]
for _ in range(M):
    kk, *connected_switches = map(int, input().split())
    k.append(kk)
    s.append(connected_switches)

p = list(map(int, input().split()))

OFF = 0
ON = 1

ans = 0
for i in range(2 ** N):
    ptn = [OFF] * N
    for j in range(N):
        if (i >> j) & 1:
            ptn[len(ptn) - j - 1] = ON

    ON_SW_COUNT_LIST = []  # 各電球に繋がったON状態のスイッチの数リスト
    for connected_switches in s:
        on_sw_cnt = len([1 for sw in connected_switches if ptn[sw - 1] == ON])
        ON_SW_COUNT_LIST.append(on_sw_cnt)

    ans += all([c % 2 == p[i] for i, c in enumerate(ON_SW_COUNT_LIST)])

print(ans)
