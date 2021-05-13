import sys, heapq
def LI(): return list(map(int, sys.stdin.readline().split()))
def LS(): return list(sys.stdin.readline())

S = LS()
T = LS()

res = 0
for i in range(3):
    if S[i] == T[i]:
        res += 1
        
print(res)