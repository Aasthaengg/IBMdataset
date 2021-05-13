import sys
input = sys.stdin.readline

a, b, k = list(map(int, input().split()))

if a > k:
    print(a-k, b)
else:
    print(0, max(b-(k-a), 0))