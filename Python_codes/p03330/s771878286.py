import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,C = LI()
D = [[0]*(C+1)] + [[0]+LI() for _ in range(C)]
c = [[0]*(N+1)] + [[0]+LI() for _ in range(N)]

from collections import defaultdict

d0,d1,d2 = defaultdict(int),defaultdict(int),defaultdict(int)
# dk = ((i+j)%3==k たる (i,j) に対して各色が何個ずつあるか)
for i in range(1,N+1):
    for j in range(1,N+1):
        if (i + j) % 3 == 0:
            d0[c[i][j]] += 1
        elif (i + j) % 3 == 1:
            d1[c[i][j]] += 1
        elif (i + j) % 3 == 2:
            d2[c[i][j]] += 1

ans = 10**18
# 変化後の色で全探索
for i in range(1,C+1):
    for j in range(1,C+1):
        for k in range(1,C+1):
            if i == j or j == k or k == i:
                continue
            else:
                a = 0
                for color in d0.keys():
                    a += D[color][i]*d0[color]
                for color in d1.keys():
                    a += D[color][j]*d1[color]
                for color in d2.keys():
                    a += D[color][k]*d2[color]
                ans = min(ans,a)

print(ans)