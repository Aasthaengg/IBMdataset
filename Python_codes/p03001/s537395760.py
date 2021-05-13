import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    w,h,x,y = LI()
    area = w * h
    ans1 = area /2
    ans2 = 0
    if w == 2*x and h == 2*y:
        ans2 = 1

    print(ans1,ans2)

main()