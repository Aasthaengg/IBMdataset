D, G = map(int, input().split())
p = []
c = []
for _ in range(D):
    p_i, c_i = map(int, input().split())
    p.append(p_i)
    c.append(c_i)
answer = 10 ** 10

for bit in range(2 ** D):
    score, solution_count, rest_max = 0, 0, 0
    for i in range(D):
        if bit & (1 << i):
            score += 100 * (i + 1) * p[i] + c[i]
            solution_count += p[i]
        else:
            rest_max = i + 1

    if score < G and rest_max:
        if (G - score) % (100 * rest_max) == 0:
            need_count = (G - score) // (100 * rest_max)
        else:
            need_count = (G - score) // (100 * rest_max) + 1
        if need_count > p[rest_max - 1]:
            continue
        else:
            score += 100 * rest_max * need_count
            solution_count += need_count

    if score >= G:
        answer = min(answer, solution_count)
print(answer)
