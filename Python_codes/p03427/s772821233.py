import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = input()

sN = set(N)
if len(N) == 1:
    ans = int(N)
elif len(N) > 1 and N[1:] == "9" * (len(N) - 1):
    ans = sum(map(int, list(N)))
else:
    ans = (len(N) - 1) * 9
    fst = int(N[0]) - 1
    ans += fst
print(ans)