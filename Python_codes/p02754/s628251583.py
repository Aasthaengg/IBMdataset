import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,a,b = map(int, input().split())

print(n // (a + b) * a + min(n % (a + b), a))
