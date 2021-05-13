S = input()
# sを最後に残す文字にして全探索してみる
cnt = 10 ** 9
for s in S:
    nex = list(S)
    tmp = 0
    while len(set(nex)) > 1:
        tmp += 1
        L = len(nex)
        now = nex
        nex = []
        for i in range(L-1):
            if s in now[i:i+2]:
                nex.append(s)
            else:
                nex.append(now[i])
    cnt = min(cnt, tmp)
print(cnt)

