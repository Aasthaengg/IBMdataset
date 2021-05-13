import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def main():
    n = int(input())
    aa = list(map(int, input().split()))
    ave = sum(aa) / n
    mn = 1000
    mi = 0
    for i, a in enumerate(aa):
        if abs(ave - a) < mn:
            mn = abs(ave - a)
            mi = i
    print(mi)

main()
