import sys;      from decimal import Decimal
import math;     from itertools import combinations, product
import bisect;   from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 6 + 7
INF = 10 ** 9
PI = 3.14159265358979323846

def read_str():      return sys.stdin.readline().strip()
def read_int():      return int(sys.stdin.readline().strip())
def read_ints():     return map(int, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def lcm(a: int, b: int) -> int: return (a * b) // math.gcd(a, b)

def Main():
    n = read_int()
    testimony = [[] for _ in range(n)]
    ans = 0

    for i in range(n):
        for _ in range(read_int()):
            x, y = read_ints()
            testimony[i].append((x-1, y))
    
    for bit in range(1 << n):
        flag = True
        for i in range(n):
            if (bit >> i) & 1:
                for x, y in testimony[i]:
                    if (bit >> x) & 1 != y:
                        flag = False
                        break
                else:
                    continue
                break
        
        if flag:
            ans = max(ans, bin(bit).count('1'))
    
    print(ans)


if __name__ ==  '__main__':
    Main()