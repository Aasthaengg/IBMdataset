import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, k = map(int, read().split())

A = [i for i in range(a, min((a + k), b+1))]
B = [i for i in range(max((b - k + 1), a), b+1)]
print(*sorted(set(A+B)), sep='\n')
