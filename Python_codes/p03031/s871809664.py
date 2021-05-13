N, M = map(int, input().split())
bulb = []
count = 0

for _ in range(M):
    tmp = list(map(int, input().split()))
    bulb.append(tmp[1:])

P = list(map(int, input().split()))

for i in range(2 ** N):
    switch = []
    for j in range(N):  # スイッチの押し方を全探索
        if (i >> j) & 1:
            switch.append(j+1)
    bulb_count = M
    for k in range(M):  # M個の電球それぞれがついているか判定
        tmp = bulb[k]  # tmpは電球k につながっているスイッチ
        switch_count = 0
        for num in tmp:  # 電球kのスイッチについて判定
            if num in switch:
                switch_count += 1
        if switch_count % 2 == P[k]:
            bulb_count -= 1
    if bulb_count == 0:
        count += 1

print(count)
