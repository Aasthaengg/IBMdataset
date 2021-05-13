import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n, k = LI()
    h = [I() for _ in range(n)]
    h.sort()
    ans = float("inf")

    for i in range(n-(k-1)):
        ans = min(ans, h[i+k-1]-h[i])
    
    print(ans)
main()
