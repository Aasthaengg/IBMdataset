import math
# N = int(input())
D, G = [int(i) for i in input().split()]
problems = []
for i in range(D):
    p, c = [int(_) for _ in input().split()]
    bit = 0
    problems.append([p, c])

ans = 1001
for i in range(2**D):
    score = 0
    p_num = 0
    for j, p in enumerate(problems):
        if i >> j & 1:
            score += p[0] * 100 * (j + 1) + p[1]
            p_num += p[0]
    if score < G:
        rest = G - score
        for j in range(D-1, -1, -1):
            if i >> j & 1:
                continue
            n = math.ceil(rest / (100 * (j + 1)))
            if n <= problems[j][0] - 1:
                rest -= n * 100 * (j + 1)
                p_num += n
                break
            rest -= problems[j][0] * 100 * (j + 1)
            p_num += problems[j][0]
        if rest <= 0:
            ans = min(ans, p_num)
    else:
        ans = min(ans, p_num)
print(ans)
