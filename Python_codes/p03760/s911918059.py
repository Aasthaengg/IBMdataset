import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

O = input()
E = input()

ans = ""
for i in range(len(O)):
    if i < len(E):
        ans += O[i] + E[i]
    else:
        ans += O[i]
print(ans)
