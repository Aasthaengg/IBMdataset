import sys
input = sys.stdin.buffer.readline


N, i = map(int, input().split())
print(N-i+1)