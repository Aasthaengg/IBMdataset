import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

S = input()

ans = INF
for a1, a2, a3 in zip(S, S[1:], S[2:]):
    num = int(a1 + a2 + a3)
    tmp = abs(num - 753)
    ans = min(ans, tmp)
print(ans)