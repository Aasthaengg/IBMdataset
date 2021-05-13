N, K = map(int, input().split())

cnt = 0
cnt2 = 0
for k in range(1, N + 1):
    if k % K == 0:
        cnt += 1
    elif K % 2 == 0 and k % K == K // 2:
        cnt2 += 1

print(cnt ** 3 + cnt2 ** 3)
