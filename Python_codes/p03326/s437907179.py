import sys,queue,math,copy,itertools,bisect,collections,heapq
LI = lambda : [int(x) for x in sys.stdin.readline().split()]

N,M = LI()
cake = [LI() for _ in range(N)]

ans = 0
for b in range(8):
    b0 = b % 2
    b1 = (b//2) % 2
    b2 = (b//4) % 2
    c = [(x[0]*(b0*2-1) + x[1]*(b1*2-1) + x[2]*(b2*2-1),x) for x in cake]
    c.sort(reverse=True)
    tmp = [0,0,0]
    for i in range(M):
        for j in range(3):
            tmp[j] += c[i][1][j]

    ans = max(ans,abs(tmp[0])+abs(tmp[1])+abs(tmp[2]))

print (ans)

