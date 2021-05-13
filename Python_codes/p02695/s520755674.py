import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import combinations_with_replacement
def main():
    n, m, q = map(int, input().split())
    abcd = []
    for _ in range(q):
        q = tuple(map(int, input().split()))
        abcd.append(q)
    c1 = tuple(combinations_with_replacement(range(1,m+1), n))
    r = 0
    for ce in c1:
        t = 0
        for qe in abcd:
            a, b, c, d = qe
            a -= 1
            b -= 1
            if ce[b] - ce[a] == c:
                t += d
        r = max(r, t)
    print(r)

if __name__ == '__main__':
    main()