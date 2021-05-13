import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, S, T = read().split()
N = int(N)

def test(n):
    overlap = N + N - n
    if overlap <= 0:
        return True
    return S[-overlap:] == T[:overlap]

for n in range(N, N + N + 10):
    if test(n):
        break
print(n)