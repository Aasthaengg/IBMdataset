import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
_LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

N = NI()

d = [1 for _ in range(100)]

for i in range(1,N+1):
    j = 2
    while i > 1:
        if i % j == 0:
            d[j] += 1
            i //= j
        else:
            j += 1
n3 = 0
n5 = 0
n15 = 0
n25 = 0
n75 = 0
for x in d:
    if x >= 3: n3 += 1
    if x >= 5: n5 += 1
    if x >=15: n15 +=1
    if x >=25: n25 +=1
    if x >=75: n75 +=1
ans = (n3-n5) * ((n5) * (n5-1) // 2) + (n5) * (n5-1) * (n5-2) // 2
ans += (n5 - n15) * n15 + (n15) * (n15-1)
ans += (n3 - n25) * n25 + (n25) * (n25-1)
ans += n75
print (ans)

