import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())

lucas = [2, 1]

if N == 1:
    print(1)
    quit()

for n in range(2, N+1):
    tmp = lucas[n-1] + lucas[n-2]
    lucas.append(tmp)

ans = lucas[N]
print(ans)

