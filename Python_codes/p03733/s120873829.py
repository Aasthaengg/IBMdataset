import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,t = LI()
    switch = LI()
    ans = t

    for i in range(1,n):
        span = switch[i] - switch[i-1]
        if span < t:
            ans += -(t-span) + t
        else:
            ans += t
    
    print(ans)

main()            
