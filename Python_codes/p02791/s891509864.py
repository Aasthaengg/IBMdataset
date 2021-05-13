import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N = I()
    P = LI()
    ans = 0
    min_num = P[0]
    for i in range(N):
        if min_num>=P[i]:
            ans += 1
            min_num = P[i]

    print(ans)

main()

