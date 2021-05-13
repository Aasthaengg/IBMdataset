import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
from bisect import bisect_left, bisect_right
#======================================================#
def main():
    n = II()
    aa = MII(); bb = MII(); cc = MII()
    aa.sort();  bb.sort();  cc.sort()
    cnt = 0
    for b in bb:
        a = bisect_left(aa, b)
        c = bisect_right(cc, b)
        cnt += (a)*(n-c)
    print(cnt)



if __name__ == '__main__':
    main()