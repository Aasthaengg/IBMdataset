import sys
from itertools import permutations
def input(): return sys.stdin.readline().strip()


def main():
    a, b, c = map(int, input().split())
    ans = 10 ** 10
    for p, q, r in list(permutations([a, b, c], 3)):
        ans = min(ans, abs(p-q) + abs(q-r))
    print(ans)



if __name__ == "__main__":
    main()
