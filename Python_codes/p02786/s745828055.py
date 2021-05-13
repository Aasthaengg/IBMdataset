import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    h = I()
    num = 1
    ans = 0
    while h>1:
        h//=2
        ans += num
        num*=2
    ans += num
    print(ans)
main()
