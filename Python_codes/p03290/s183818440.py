D, G = [int(s) for s in input().split()]
problems = [[int(s) for s in input().split()] for _ in range(D)]

result = 10 ** 8

for i in range(2 ** D):
    cnt_problem = 0
    cnt_score = 0
    for j in range(D):
        if i >> j & 1:
            cnt_score += problems[j][1] + 100 * (j + 1) * problems[j][0]
            cnt_problem += problems[j][0]

    for j in reversed(range(D)):
        if not i >> j & 1:
            for _ in range(problems[j][0]):
                if cnt_score >= G:
                    break
                else:
                    cnt_score += 100 * (j + 1)
                    cnt_problem += 1
    result = min(cnt_problem, result)

print(result)
