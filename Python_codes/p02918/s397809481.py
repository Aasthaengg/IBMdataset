# https://atcoder.jp/contests/abc140/tasks/abc140_d
n, k = map(int, input().split())

s = input()
block = 0
start = 0
seg = []
block = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        block += 1

ans = min(n - 1, block + k * 2)
print(ans)
