import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import ceil, log
def main():
    k = int(input())
    k2 = int(log(ceil(k / 10), 3)) + 1
    def getlun(n, keta, last):
        lunluns.append(n)
        if keta > k2:
            pass
        else:
            l1 = n * 10 + last
            getlun(l1, keta + 1, last)
            if last > 0:
                l2 = n * 10 + last - 1
                getlun(l2, keta + 1, last - 1)
            if last < 9:
                l3 = n * 10 + last + 1
                getlun(l3, keta + 1, last + 1)
    lunluns = []
    for i1 in range(1, 10):
        getlun(i1, 0, i1)
    lunluns.sort()
    print(lunluns[k-1])

if __name__ == '__main__':
    main()
