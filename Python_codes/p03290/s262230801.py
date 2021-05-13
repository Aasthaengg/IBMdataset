D, G = map(int, input().split())
p, c = list(zip(*[list(map(int, input().split())) for _ in range(D)]))

ans = sum(p)
for i in range(2 ** D):
    complete_indexes = [j for j in range(D) if (i >> j) & 1]

    question = 0
    point = 0
    for j in complete_indexes:
        question += p[j]
        point += p[j] * 100 * (j + 1) + c[j]

    if point < G:
        incomplete_indexes = [j for j in range(D) if j not in complete_indexes]
        if incomplete_indexes:
            index = incomplete_indexes[-1]
            required_question = (G - point + 100 * (index + 1) - 1) // (100 * (index + 1))
            question += min(required_question, p[index])
            point += min(required_question, p[index]) * 100 * (index + 1)

    if G <= point and question < ans:
        ans = question

print(ans)
