import sys; input = lambda: sys.stdin.readline()
k, s = map(int, input().split())
cnt = 0
for i in range(0, k + 1):
    for j in range(0, k + 1):
        if 0 <= s - i - j <= k:
            cnt += 1
print(cnt)