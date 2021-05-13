# -*- coding: utf-8 -*-

N, K = map(int, input().split())
A = list(map(int, input().split()))

sum_a = sum(A)
# dc:Divisor Candidate(割る数の候補)
#dc_list = [x for x in reversed(range(1, sum_a + 1)) if sum_a % x == 0]
dc_list = []
for i in range(1, int(sum_a ** 0.5) + 1):
    if sum_a % i == 0:
        dc_list.append(i)
        if i != sum_a // i:
            dc_list.append(sum_a // i)

dc_list.sort(reverse = True)

for d in dc_list:
    mods = [a % d for a in A]
    mod_sum = sum(mods)
    if mod_sum % d != 0:
        continue
    mods = sorted(mods)

    op = 0
    mod_len = len(mods)
    for i, mod in enumerate(mods):
        op += mod

        if op > K:
            break

        if (mod_len - (i + 1)) * d == mod_sum and op <= K:
            print(d)
            exit(0)
