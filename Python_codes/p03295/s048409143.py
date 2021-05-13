import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N, M = map(int, input().split())

AB = [tuple(map(int, input().split())) for _ in range(M)]

AB.sort(key = lambda x: x[1]) #右側が小さい順にソート
AB.sort(key = lambda x: x[0]) #左側が小さい順にソート

ans = 0

right = N + 1
for a, b in AB:
    if a < right:
        right = min(right, b)
    else:
        ans += 1
        right = b

print (ans + 1)

