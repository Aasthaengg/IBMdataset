import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,M = MI()
ab = [tuple(MI()) for _ in range(N)]
cd = [tuple(MI()) for _ in range(M)]

for i in range(N):
    a,b = ab[i]
    min_dis = 10**10
    k = 100
    for j in range(M):
        c,d = cd[j]
        if min_dis > abs(a-c) + abs(b-d):
            k = j+1
            min_dis = abs(a-c) + abs(b-d)
    print(k)
