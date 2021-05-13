import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,M = MI()
xv = [(0,0)] + [tuple(MI()) for _ in range(N)]

A = [0]*(N+1)  # 時計回りにi貫目までいけるとき、差し引き得られる最大キロカロリー
a = 0
for i in range(1,N+1):
    x,v = xv[i]
    x0,v0 = xv[i-1]
    a += v-(x-x0)
    if a > A[i-1]:
        A[i] = a
    else:
        A[i] = A[i-1]

B = [0]*(N+1)  # 時計回りにi貫目までいけるとき、差し引き得られる最大キロカロリー(最後初期位置に戻る)
b = 0
for i in range(1,N+1):
    x,v = xv[i]
    x0,v0 = xv[i-1]
    b += v-2*(x-x0)
    if b > B[i-1]:
        B[i] = b
    else:
        B[i] = B[i-1]

for i in range(1,N+1):
    x,v = xv[i]
    xv[i] = (M-x,v)
xv.sort()

C = [0]*(N+1)  # 反時計回りにi貫目までいけるとき、差し引き得られる最大キロカロリー
c = 0
for i in range(1,N+1):
    x,v = xv[i]
    x0,v0 = xv[i-1]
    c += v-(x-x0)
    if c > C[i-1]:
        C[i] = c
    else:
        C[i] = C[i-1]

D = [0]*(N+1)  # 反時計回りにi貫目までいけるとき、差し引き得られる最大キロカロリー(最後初期位置に戻る)
d = 0
for i in range(1,N+1):
    x,v = xv[i]
    x0,v0 = xv[i-1]
    d += v-2*(x-x0)
    if d > D[i-1]:
        D[i] = d
    else:
        D[i] = D[i-1]

ans = 0
for i in range(N+1):
    ans = max(ans,A[i]+D[N-i])
    ans = max(ans,C[i]+B[N-i])
print(ans)
