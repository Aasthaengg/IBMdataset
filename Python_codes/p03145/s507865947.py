import sys
INF = 10 ** 10
MOD = 10 ** 9 + 7
from functools import lru_cache
sys.setrecursionlimit(100000000)

def main():
    a,b,c = map(int,input().split())
    print(a * b //2)
if __name__ =='__main__':
    main()   