import sys
from operator import itemgetter

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Cut = [[int(i) - 1 for i in input().split()] for _ in range(M)]
    Cut.sort(key = itemgetter(1))
    count = 1
    cindex = 1
    cutPlace = Cut[0][1]
    while cindex < M:
        if Cut[cindex][0] < cutPlace: cindex += 1
        else:
            count += 1
            cutPlace = Cut[cindex][1]
            cindex += 1
    print(count)

    return 0

if __name__ == "__main__":
    solve()