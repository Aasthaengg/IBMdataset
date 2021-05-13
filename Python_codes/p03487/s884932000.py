import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A: d[a] += 1
    ans = 0
    for key in d:
        if d[key] < key:
            ans += d[key]
            continue
        ans += d[key] - key
    print(ans)



if __name__ == "__main__":
    main()
