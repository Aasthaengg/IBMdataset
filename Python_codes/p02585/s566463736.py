N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

point_loop_list = [0 for _ in range(N)]
point_set = set()
loop_list = []
for i in range(N):
    if i in point_set:
        continue
    loop = [i]
    j = P[i] - 1
    while j != i:
        loop.append(j)
        point_set.add(j)
        j = P[j] - 1
    loop += loop
    loop_list.append(loop)

# print(loop_list)

loop_sum_list = [0 for _ in range(N)]

for loop in loop_list:
    loop_len = len(loop) // 2
    s = sum([C[j] for j in loop[:loop_len]])

    for i, p in enumerate(loop[:loop_len]):
        point_loop_list[p] = loop[i:i+loop_len]
        loop_sum_list[p] = s


ans = min(C)

for l, s in zip(point_loop_list, loop_sum_list):
    p = 0
    loop_len = len(l)
    if s > 0:
        num_loop = K // loop_len if K % loop_len != 0 else K // loop_len - 1
        p += s * num_loop
        m = 0
        cs = 0
        for i in range(K - loop_len * num_loop):
            cs += C[l[i]]
            m = max(m, cs)
        p += m
    else:
        m = C[l[0]]
        cs = m
        for i in range(1, loop_len):
            cs += C[l[i]]
            m = max(m, cs)
        p += m
    ans = max(p, ans)

print(ans)

