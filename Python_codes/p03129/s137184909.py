import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if n >= (2*k - 1):
    print("YES")
else:
    print("NO")