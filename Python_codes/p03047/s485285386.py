import sys
import itertools

N, K = map(int, sys.stdin.readline().split())

ans = N - K + 1

print(ans)