N = int(input())
Fs = [list(map(int, input().split())) for i in range(N)]
Ps = [list(map(int, input().split())) for i in range(N)]

cnts = [0] * 10
for F in Fs:
    for i,f in enumerate(F):
        cnts[i] += f

ans = -10**10
for i in range(1,2**10):
    bs = list(bin(i)[2:].zfill(10))
    cnt_all = 0
    for fs,ps in zip(Fs, Ps):
        cnt = 0
        for i in range(10):
            if int(bs[i]) * int(fs[i]) == 1:
                cnt += 1
        cnt_all += ps[cnt]
    ans = max(cnt_all,ans)
    # print(bs,cnt)
print(ans)