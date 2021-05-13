import sys
sys.setrecursionlimit(10**7)
#input = sys.stdin.readline
from collections import Counter

def main():
    a = input()
    n = len(a)

    base = n * (n - 1) // 2
    counter = Counter(a)

    def f():
        for c in counter.values():
            yield c * (c - 1) // 2

    print(base - sum(f()) + 1)

main()