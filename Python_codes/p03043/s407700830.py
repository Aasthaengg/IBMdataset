import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,k = LI()
    num = 0
    frac = 0
    while n * 2**num < k:
        num+=1
    frac += 1/2**num
    # print(frac)

    for i in range(n-1,0,-1):
        while i * 2**num < k:
            num += 1
        frac += 1/2**num
    
    ans = frac * (1/n)
    print(ans)
main()