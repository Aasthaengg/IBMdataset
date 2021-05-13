N, K = map(int, input().split())

result = 0
for i in range(1, N+1):
    score = i
    sub_prob_recip = N
    while score < K:
        sub_prob_recip *= 2
        score *= 2
    result += 1/sub_prob_recip

print(result)
