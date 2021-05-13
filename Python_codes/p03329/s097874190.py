N = int(input())
ans = 10**13
Y = [9**i for i in range(1, 10)] + [6**i for i in range(1, 10)]
Y = sorted(Y, reverse=True)
for i in range(N+1):
    tmp = 0
    n = N-i
    for j in range(10, -1, -1):
        if i // 9**j > 0:
            tmp += i // 9**j
            i %= 9**j
    for j in range(10, -1, -1):
        if n // 6**j > 0:
            tmp += n // 6**j
            n %= 6**j
        # print(ans, j)

        # print(ans, j, N)
    ans = min(ans, tmp)

print(ans)