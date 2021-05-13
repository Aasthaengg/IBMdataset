import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
MIN = 10**18
for i in range(1, N):
    val = 0
    a, b = i, N-i
    while a or b:
        x = a%10
        y = b%10
        val += (x+y)
        a //=10
        b //= 10
    MIN = min(MIN, val)

print(MIN)