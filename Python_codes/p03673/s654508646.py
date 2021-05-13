import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    n = I()
    a = LI()
    if n % 2 == 0:
        print(*a[::-2],*a[::2])
    else:
        print(*a[::-2],*a[1::2])
main()