from itertools import combinations
from collections import defaultdict
def main():
    n = int(input())
    march = defaultdict(int)

    for _ in range(n):
        s = input()
        march[s[0]] += 1

    p = tuple(combinations(['M', 'A', 'R', 'C', 'H'], 3))
    r = 0
    for pe in p:
        t = march[pe[0]] * march[pe[1]] * march[pe[2]]
        r += t
    print(r)

if __name__ == '__main__':
    main()
