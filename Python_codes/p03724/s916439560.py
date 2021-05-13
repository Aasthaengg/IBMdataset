import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
cnt = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    cnt[a] ^= 1
    cnt[b] ^= 1

if all(x == 0 for x in cnt):
    print("YES")
else:
    print("NO")