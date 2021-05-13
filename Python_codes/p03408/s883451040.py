import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    dict = defaultdict(int)
    for _ in range(N):
        string = input()
        dict[string] += 1
    M = int(input())
    for _ in range(M):
        string = input()
        dict[string] -= 1

    ans = 0
    for key in dict: ans = max(ans, dict[key])
    print(ans)


if __name__ == "__main__":
    main()
