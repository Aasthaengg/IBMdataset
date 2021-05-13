# import sys
# input = sys.stdin.readline

N,M,Q = map(int,input().split())

com = [[0] * 502 for i in range(502)]

for _ in range(M):
    L,R = map(int,input().split())
    com[L][R] += 1

for i in range(502):
    for j in range(1,502):
        com[i][j] += com[i][j-1]

for _ in range(Q):
    p,q = map(int,input().split())
    ans = 0
    for i in range(p,q+1):
        ans += com[i][q]
    print(ans)
