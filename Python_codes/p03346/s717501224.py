N = int(input())
idx = {int(input()): i for i in range(N)}
res = N - 1
cnt = 1
for x in range(2, N + 1):
    if idx[x - 1] < idx[x]:
        cnt += 1
    else:
        res = min(res, N - cnt)
        cnt = 1
print(min(res, N - cnt))