import itertools

N,A,B,C = map(int,input().split())
L = [int(input()) for _ in range(N)]

INF = 10**18
ans = INF

for ptn in itertools.product([0,1,2,3], repeat=N):
    x = [0] * 4
    MP = 0
    for take, length in zip(ptn, L):
        if take == 3:  # 使わない
            continue
        if x[take] != 0:
            MP += 10
        x[take] += length
    if x[0]==0 or x[1]==0 or x[2]==0:
        continue
    MP += abs(A-x[0])
    MP += abs(B-x[1])
    MP += abs(C-x[2])
    if ans > MP:
        ans = MP
print(ans)