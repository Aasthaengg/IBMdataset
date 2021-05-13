import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():

    k, t = LI()
    a = LI()
    a.sort(reverse=True)

    ans = max(a[0]-1-sum(a[1:]), 0)
    print(ans)


main()
