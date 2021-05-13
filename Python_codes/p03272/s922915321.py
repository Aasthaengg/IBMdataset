import sys
sys.setrecursionlimit(5 * 10**5)
input = sys.stdin.readline

N, i = list(map(int, input().split()))

print(N - i + 1)
