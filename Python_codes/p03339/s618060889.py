N = int(input())
S = input()

sum_W = [0] * (N+1)
sum_E = [0] * (N+1)

for i in range(N):
    if S[i] == "W":
        sum_W[i+1] = sum_W[i] + 1
        sum_E[i+1] = sum_E[i]
    else:
        sum_W[i+1] = sum_W[i]
        sum_E[i+1] = sum_E[i] + 1

answers = []
for i in range(N):
    answer = sum_W[i] + (sum_E[N] - sum_E[i+1])
    answers.append(answer)

print(min(answers))