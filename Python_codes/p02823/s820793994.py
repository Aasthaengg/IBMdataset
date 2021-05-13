import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n, a, b = LI()
    a, b = min(a,b), max(a,b)
    ans = 0
    if (b-a)%2 == 0:
        ans = (b-a)//2
    else:
        ans = min(a+(b-a-1)//2, n-b+1+(n-(a+n-b+1))//2)
    print(ans)
main()
