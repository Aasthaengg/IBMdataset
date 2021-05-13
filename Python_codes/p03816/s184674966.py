import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A: d[a] += 1
    kind = [0] * 2
    for key in d: kind[d[key] % 2] += 1
    if kind[0] % 2 == 0:
        print(sum(kind))
    else:
        print(sum(kind) - 1)





if __name__ == "__main__":
    main()
