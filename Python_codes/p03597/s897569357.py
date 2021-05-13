import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

N, = map(int, input().split())
A, = map(int, input().split())

print(N ** 2 - A)