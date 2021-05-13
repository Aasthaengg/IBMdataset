import sys

N,C = [int(x) for x in input().split()]
X=[]
V=[]
for _ in range(N):
    x,v = [int(x) for x in input().split()]
    X.append(x)
    V.append(v)

# 右回りの累積和
s = 0
r = [0]*N
for i in range(N):
    s += V[i]
    r[i] = s - X[i]

# 左回りの累積わ
s = 0
l = [0]*N
for i in range(N):
    s += V[N-1-i]
    l[N - 1 - i] = s - (C - X[N - 1 - i])

# 原点～iのMax(R)
MaxR = [0] * N
MaxR[0] = r[0]
for i in range(1,N):
    MaxR[i] = max(MaxR[i-1], r[i])

# 原点～iのMax(L)
MaxL = [0] * N
MaxL[N-1] = l[N-1]
for i in range(1,N):
    MaxL[N-1-i] = max(MaxL[N-i], l[N-1-i])

a = max(r)
b = max(l)
c, d = 0, 0
if N>1:
    c = max([r[i] - X[i] + MaxL[i + 1] for i in range(N - 1)])
    d = max([l[i] - (C-X[i]) + MaxR[i - 1] for i in range(N - 1,0,-1)])

print(max([a,b,c,d,0]))
