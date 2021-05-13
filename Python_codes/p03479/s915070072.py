import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    x, y = LI()
    ans = 1
    cnt = x
    while cnt*2<=y:
        ans += 1
        cnt *= 2
    print(ans)
main()
