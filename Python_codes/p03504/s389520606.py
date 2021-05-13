# ABC080 D - Recording
N,C = map(int,input().split())
T = [[0 for _ in range(C)] for j in range(100001)]
for i in range(N):
    s,t,c = map(int,input().split())
    for j in range(s-1,t):
        T[j][c-1] = 1
ans = 0
for i in range(100001):
    sumT = sum(T[i])
    if ans < sumT:
        ans = sumT
print(ans)