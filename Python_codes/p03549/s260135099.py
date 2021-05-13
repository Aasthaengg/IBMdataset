import sys
input = sys.stdin.readline

N, M = map(int, input().split())

d = 2 ** M
print((1900*M+100*(N-M))*d)