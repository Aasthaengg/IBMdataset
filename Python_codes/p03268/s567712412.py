N, K = map(int, (input().split()))
ans_zero = set()
ans_notzero = set()
for i in range(1, N+1):
    if i % K == 0:
        ans_zero.add(i)

    elif i % K == K / 2:
        ans_notzero.add(i)

print(len(ans_zero) ** 3 + len(ans_notzero) ** 3)