N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for n in range(N)]

cnt = 0
for a in A:
    calc = 0
    for m in range(M):
        calc += a[m] * B[m]
    if calc + C > 0:
        cnt += 1

print(cnt)
