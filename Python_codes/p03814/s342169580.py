import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

S = input()

a_index = INF
b_index = 0
for i, s in enumerate(S):
    if a_index == INF and s == "A":
        a_index = i
    if s == "Z":
        b_index = i

ans = b_index - a_index + 1
print(ans)
