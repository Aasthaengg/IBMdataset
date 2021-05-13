import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *
from math import *
from fractions import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    states = [s + t + u for s in 'ACGT' for t in 'ACGT' for u in 'ACGT']
    states.remove('AGC')
    states.remove('ACG')
    states.remove('GAC')
    transitions = defaultdict(list)
    ngs = []
    for s in 'ACGT':
        for t in 'ACGT':
            for u in 'ACGT':
                for v in 'ACGT':
                    if 'AGC' in s + t + u + v or 'AGC' in t + s + u + v or 'AGC' in s + u + t + v or 'AGC' in s + t + v + u:
                        ngs.append(s + t + u + v)
    for s in states:
        for t in states:
            if s[1:] == t[:2] and s[0] + t not in ngs:
                transitions[s].append(t)
    count = {s: 1 for s in states}
    for _ in range(N - 3):
        updated = {s: 0 for s in states}
        for fr, tos in transitions.items():
            for to in tos:
                updated[to] += count[fr]
                updated[to] %= 10 ** 9 + 7
        count = updated
    print(sum(count.values()) % (10 ** 9 + 7))

main()
