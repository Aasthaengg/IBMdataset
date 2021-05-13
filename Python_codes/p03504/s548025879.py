import numpy as np

n,c = map(int,input().split())
table = np.zeros(10**5+2, dtype=np.int32)
chs = [[] for _ in range(c+1)]

for _ in range(n):
    s,t,c = map(int,input().split())
    chs[c].append([s,t])

# 同チャンネル内の連続番組を合体
times = []
for ch in chs:
    if not ch: continue
    ch.sort()
    for i in range(len(ch)):
        if i == 0: continue
        if ch[i-1][1] == ch[i][0]:
            ch[i] = [ch[i-1][0], ch[i][1]]
            ch[i-1] = []
    for arr in ch:
        if not arr: continue
        times.append(arr)

# いもす法
for arr in times:
    table[arr[0]] += 1
    table[arr[1]+1] -= 1

# 累積和の最大値
ans = table.cumsum().max()

print(ans)

