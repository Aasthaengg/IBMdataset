import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,m,c = LI()
    b = LI()
    ans = 0
    for _ in range(n):
        a = LI()
        cul = 0
        for x, y in zip(a,b):
            cul += x*y
        cul += c
        ans += 1 if cul > 0 else 0
    
    print(ans)
main()