D, G = map(int, input().split())
p, c = list(zip(*[list(map(int, input().split())) for _ in range(D)]))

ans = sum(p)
for i in range(2 ** D):
    complete_indexes = [j for j in range(D) if (i >> j) & 1]

    cur_ans = 0
    cur_point = 0
    for j in complete_indexes:
        cur_ans += p[j]
        cur_point += p[j] * 100 * (j + 1) + c[j]

    if cur_point < G:
        incomplete_indexes = [j for j in range(D) if j not in complete_indexes]
        if incomplete_indexes:
            used_index = incomplete_indexes[-1]
            required = (G - cur_point + 100 * (used_index + 1) - 1) // (100 * (used_index + 1))
            cur_ans += min(required, p[used_index])
            cur_point += min(required, p[used_index]) * 100 * (used_index + 1)

    if G <= cur_point and cur_ans < ans:
        ans = cur_ans

print(ans)
