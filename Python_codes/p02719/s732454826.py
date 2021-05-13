N, K = map(int, input().split())

cand_1 = N % K
cand_2 = K - cand_1

min = min(cand_1, cand_2)

print(min)
