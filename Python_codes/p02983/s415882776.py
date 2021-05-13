import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    l,r = LI()
    num = r-l+1
    ans = 0
    if num < 2019:
        ans = 2020
        for i in range(l,r+1):
            for j in range(i+1,r+1):
                ans = min(ans,i*j%2019)

    print(ans)
main()