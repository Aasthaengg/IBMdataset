from itertools import product

d, g = map(int, input().split())
prob = []
for i in range(1, d + 1):
    p, c = map(int, input().split())
    prob.append((i * 100, p, c))  # score, num, bonus

ans = 1000000000
# repeatは
for prd in product([0, 1], repeat=d):
    cnt = 0
    allScore = 0
    for j, (score, num, bonus) in zip(prd, prob):
        if j == 1:
            cnt += num
            allScore += score * num + bonus

    if allScore < g:
        for j, (score, num, bonus) in zip(prd, prob):
            if j == 0 and (score * num >= g - allScore):
                rest = (g - allScore) // score
                cnt += rest
                allScore += score * rest
                break

    if allScore >= g:
        ans = min(ans, cnt)

print(ans)
