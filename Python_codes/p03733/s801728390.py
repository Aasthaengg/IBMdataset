N, T = map(int, input().split())
t = list(map(int, input().split()))

sum_second = 0
for i in range(N):
    if (i == N - 1):
        sum_second += T
        break

    if (t[i + 1] - t[i] <= T):
        sum_second += t[i + 1] - t[i]
    else:
        sum_second += T

    # if T > t[i + 1] - sum_second:
    #     sum_second += t[i + 1] - sum_second
    # elif (T <= t[i + 1] - sum_second):
    #     sum_second += T


print(sum_second)
