from sys import stdin
from collections import defaultdict
from math import sqrt

def main():
    input = stdin.readline

    h = defaultdict(int)
    h[2] = 1
    for i in range(3, 100000, 2):
        for j in range(3, int(sqrt(i)) + 1, 2):
            while i % j == 0:
                h[j] = 1
                i //= j
        if i > 1:
            h[i] = 1
    k = [0] * 100001
    for key in h.keys():
        if (key + 1) / 2 in h and h[(key + 1) / 2] == 1:
            k[key] = 1
    for i in range(1, 100001):
        k[i] += k[i - 1]
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        print(k[r] - k[l - 1])
main()