# 93 C - Switches
N,M = map(int,input().split())
K = []
S = []
for _ in range(M):
    s = list(map(int,input().split())) 
    K.append(s[0])
    # 0-indexed
    s = [i-1 for i in s]
    S.append(s[1:])
P = list(map(int,input().split()))

ans = 0
for i in range(1<<N):
    swiches = [0]*N
    for j in range(N):
        mask = 1<<j
        # j 番目のスイッチが on のとき
        if i & mask != 0:
            swiches[j] = 1
        # j 番目のスイッチが off のとき
        else:
            continue

    # on の電球をカウント
    cnt_light = 0
    for m in range(M):
        cnt_swich = 0
        for s in S[m]:
            if swiches[s] == 1:
                cnt_swich += 1
        if cnt_swich%2 == P[m]:
            cnt_light += 1
    if cnt_light == M:
        ans += 1
print(ans)