import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
_LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

N,K = LI()
A = LI()
max_bit = (10**12).bit_length()
bit = [0 for _ in range(max_bit)]
for x in A:
    b = 1
    for j in range(max_bit):
        if x & b: bit[j] += 1
        b <<= 1

ans = 0
k = 0
for i in range(max_bit-1,-1,-1):
    b = bit[i]
    if k + 2**i <= K and bit[i]*2 < N:
        b = N - b
        k += 2**i
    ans += b * 2**i
print (ans)


