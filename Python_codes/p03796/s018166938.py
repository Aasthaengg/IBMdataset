import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    import math
    n=int(input())
    print(math.factorial(n)%(10**9+7))
resolve()