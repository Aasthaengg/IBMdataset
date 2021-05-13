N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
count = 0
for a in A:
    ans = 0
    for i in range(M):
        ans += a[i] * B[i]
    if ans + C > 0:
        count += 1
print(count)