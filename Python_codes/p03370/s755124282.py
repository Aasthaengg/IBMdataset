N_syu, X_gram = map(int, input().split())

weight = [int(input()) for i in range(N_syu)]

module = X_gram - sum(weight)
ans = N_syu + module // min(weight)

print(ans)
