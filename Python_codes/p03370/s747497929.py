N, X = map(int, input().split())
M = [int(input()) for i in range(N)]
cnt = 0
for i in M:
    X -= i
    cnt += 1
while True:
    X -= min(M)
    if X < 0:
        break
    cnt += 1
print(cnt)