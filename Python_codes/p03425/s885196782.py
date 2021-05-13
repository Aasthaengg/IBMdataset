import sys
from itertools import combinations
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    d = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
    for _ in range(n):
        c = input()
        if c[0] in d: d[c[0]] += 1
    #print(d)
    ans = 0
    for a, b, c in combinations(['M', 'A', 'R', 'C', 'H'], 3):
        ans += d[a] * d[b] * d[c]
    print(ans)

if __name__ == "__main__":
    main()
