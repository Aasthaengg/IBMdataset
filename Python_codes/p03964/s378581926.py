def examC():
    N = I()
    cur = [1,1]
    for i in range(N):
        T, A = LI()
        k = max((cur[0]+T-1)//T,(cur[1]+A-1)//A)
        cur[0] = T * k
        cur[1] = A * k
#        print(cur)
    print(sum(cur))



import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
