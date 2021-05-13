N = int(input())
p = list(map(int, input().split()))

cnt = 1
min_p = p[0]
for i in range(1, N):
    if min_p >= p[i]:
        cnt += 1
    min_p = min(min_p, p[i])
print(cnt)