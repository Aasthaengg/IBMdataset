import sys
input = sys.stdin.readline

n, r = map(int, input().split())
print(r + 100 * (10 - min(10, n)))