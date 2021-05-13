import sys
import itertools
import copy
from collections import defaultdict

input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    N, K = MI()
    index = 0
    d = defaultdict(int)
    for i in range(N):
        a, b = MI()
        d[a] += b
    d = sorted(d.items(), key=lambda x:x[0])
    for i in d:
        index += i[1]
        if index >= K:
            print(i[0])
            sys.exit()
        
        
main()