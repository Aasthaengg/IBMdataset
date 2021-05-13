import numpy as np
N, H = map(int,input().split())

maxA = 0
B = []
for _ in range(N):
    a, b = map(int,input().split())
    B.append(b)
    if maxA < a:
        maxA = a

B = np.array(B)
throw_all = np.sort((B[B>maxA]))[::-1]
SUM = 0
cnt = 0
for a in throw_all:
    SUM += a
    cnt += 1
    if SUM >= H:
        print(cnt)
        exit()

ans = -(-(H-SUM)//maxA)+ cnt
print(ans)
