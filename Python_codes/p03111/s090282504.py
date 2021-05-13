import sys
from itertools import product
N, A, B, C = map(int, sys.stdin.readline().rstrip().split())
L = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
ans = 10**4

for cmb in product(range(4), repeat=N):
    a_sum = 0
    b_sum = 0
    c_sum = 0
    flag_a = 0
    flag_b = 0
    flag_c = 0
    cnt = 0
    for c, l in zip(cmb, L):
        if c == 0:
            a_sum += l
            if flag_a:
                cnt += 1
            else:
                flag_a = 1
        elif c == 1:
            b_sum += l
            if flag_b:
                cnt += 1
            else:
                flag_b = 1
        elif c == 2:
            c_sum += l
            if flag_c:
                cnt += 1
            else:
                flag_c = 1
    if flag_a == flag_b == flag_c == 1:
        ans = min(ans, 10 * cnt + abs(a_sum - A) + abs(b_sum - B) + abs(c_sum - C))
print(ans)