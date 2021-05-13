import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, readline().split())
S = list(read().rstrip().decode())

S[K - 1] = S[K - 1].lower()
print(''.join(S))