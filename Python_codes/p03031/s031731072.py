N, M = map(int, input().split())
switches_bulbs_connection = {}

for i in range(M):
    switches_bulbs_connection[i] = list(map(int, input().split()))[1:]
p = list(map(int, input().split()))
count = 0
flag = 0

for i in range(2 ** N):  # スイッチのon/offについてビット全探索
    switch_on_off = [0] * N
    bulb_stat = [0] * M
    for j in range(N):
        if (i >> j) & 1:
            switch_on_off[j] += 1  # 各スイッチがonかoffか
    for k in range(M):  # 電球kについて調べる
        tmp = switches_bulbs_connection[k]
        for switch in tmp:
            if switch_on_off[switch-1]:
                bulb_stat[k] += 1
    for l in range(M):
        if bulb_stat[l] % 2 == p[l]:
            flag += 1
    if flag == M:
        count += 1
    flag = 0

print(count)
