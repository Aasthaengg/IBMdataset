import sys
read = sys.stdin.buffer.read
readlines = sys.stdin.buffer.readlines
input = sys.stdin.buffer.readline
H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in [0]*10]
A = map(int, read().split())

for i in range(10):
    for j in range(10):
        for k in range(10):
            dist = C[j][i] + C[i][k]
            if C[j][k] > dist:
                C[j][k] = dist

cnt = [0]*10
for a in A:
    if a != -1:
        cnt[a] += 1
ans = 0
for i, c in enumerate(cnt):
    ans += C[i][1] * c
print(ans)
