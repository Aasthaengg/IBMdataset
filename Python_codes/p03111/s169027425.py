from itertools import product
n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
# 3:A 2:B 1:C 0:使わない
ans = float("inf")
use_list = list(product(range(4), repeat=n))
#print(use_list)
for take_use in use_list:
    a, b, c = 0, 0, 0
    count_a, count_b, count_c = 0, 0, 0
    cost = 0
    for j in range(n):
        if take_use[j] == 3:
            a += l[j]
            count_a += 1
        elif take_use[j] == 2:
            b += l[j]
            count_b += 1
        elif take_use[j] == 1:
            c += l[j]
            count_c += 1
    if count_a == 0 or count_b == 0 or count_c == 0:
        continue
    cost += (count_a-1 + count_b-1 + count_c-1)*10
    cost += abs(A-a) + abs(B-b) + abs(C-c)
    ans = min(ans, cost)
print(ans)
