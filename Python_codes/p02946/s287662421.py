import sys

K, X = map(int, sys.stdin.readline().split())

left = max(-1000000, X - K + 1)
right = min(1000000, X + K - 1)
# print(left, right)
ans = [i for i in range(left, right+1)]
print(*ans)