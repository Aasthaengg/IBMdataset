import sys
input = sys.stdin.readline
INF = 10**10
MOD = 10**9 + 7
sys.setrecursionlimit(100000000)
from functools import lru_cache
from itertools import permutations

def main():
    t,x = map(int,input().split())
    print(t/x)
if __name__=='__main__':
    main() 