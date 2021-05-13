S = input()
n = len(S)

answer = 0
for i in range(2 ** (n - 1)):
    total_sum = 0
    tmp = S[0]
    for j in range(n - 1):
        if (1 << j) & i:
            total_sum += int(tmp)
            tmp = S[j + 1]
        else:
            tmp += S[j + 1]
    total_sum += int(tmp)
    answer += total_sum

print(answer)