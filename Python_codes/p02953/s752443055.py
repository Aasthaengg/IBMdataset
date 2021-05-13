import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    h = LI()
    mx = h[0]

    for x in h[1:]:
        if mx-1 <= x:
            pass
            mx = max(mx, x)
        else:
            print("No")
            break
    else:
        print("Yes")
main()
