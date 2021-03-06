import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from collections import defaultdict
def main():
    n = int(input())
    a = list(map(int, input().split()))

    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for i, ae in enumerate(a):
        d1[i + ae +1] += 1
        d2[i - ae +1] += 1
    r = 0
    for d1e in d1.keys():
        rt = d1[d1e] * d2[d1e]
        r += rt
    print(r)

if __name__ == '__main__':
    main()