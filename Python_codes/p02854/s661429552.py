N = int(input())
A = list(map(int, input().split()))

cumsum = [0]
for i in range(N):
    cumsum.append(cumsum[-1] + A[i])

tmp_x = -1
tmp_x_diff = -1
for i in range(N - 1):
    sum1 = cumsum[i + 1]
    sum2 = cumsum[-1] - cumsum[i + 1]
    diff = abs(sum2 - sum1)
    if tmp_x_diff == -1 or diff < tmp_x_diff:
        tmp_x = i
        tmp_x_diff = diff
print(tmp_x_diff)
