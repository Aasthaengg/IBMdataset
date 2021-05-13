import sys;      from decimal import Decimal
import math;     from itertools import combinations, product
import bisect;   from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846

def read_str():      return sys.stdin.readline().strip()
def read_int():      return int(sys.stdin.readline().strip())
def read_ints():     return map(int, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def lcm(a: int, b: int) -> int: return (a * b) // math.gcd(a, b)

def Main():
    n, m = read_ints()
    py = []
    for i in range(m):
        p, y = read_ints()
        py.append([y, p, i])
    py.sort(key=lambda x: x[0])  
    cnt = [0] * n
    ans = [''] * m
    
    for year, prefecture, idx in py:
        cnt[prefecture - 1] += 1
        ans[idx] = f'{prefecture:06d}{cnt[prefecture-1]:06d}'

    print(*ans, sep='\n')        

if __name__ ==  '__main__':
    Main()