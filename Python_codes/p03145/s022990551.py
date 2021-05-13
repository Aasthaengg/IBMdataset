import sys
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()


def main():
    p, q, r = map(int, input().split())
    print(p * q // 2)



if __name__ == "__main__":
    main()
