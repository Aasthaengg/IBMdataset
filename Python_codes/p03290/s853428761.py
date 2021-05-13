D, G = map(int, input().split())
p = []
c = []
for _ in range(D):
    p_i, c_i = map(int, input().split())
    p.append(p_i)
    c.append(c_i)
answer = 10000000

for bit in range(2 ** D):
    s, num, rest_max = 0, 0, 0
    for i in range(D):
        if bit & (1 << i):
            s += 100 * (i + 1) * p[i] + c[i]
            num += p[i]
        else:
            rest_max = i
    if s < G:
        s1 = 100 * (rest_max + 1)
        if (G - s) % s1 == 0:
            need = (G - s) // s1
        else:
            need = (G - s) // s1 + 1
        if need >= p[rest_max]:
            continue
        num += need
    answer = min(answer, num)
print(answer)
