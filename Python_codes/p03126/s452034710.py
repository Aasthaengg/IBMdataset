N, M = map(int, input().split())
cnt = [0] * M

for i in range(N):
    line = list(map(int, input().split()))[1:]
    for j in line:
        cnt[j-1] += 1

ans = sum([1 if i == N else 0 for i in cnt])
print(ans)
