N = int(input())
A = list(map(int, input().split()))

A = [a // 400 for a in A]

C = [0 for _ in range(9)]
for a in A:
    if a > 8:
        a = 8
    C[a] += 1

cnt_0 = 0
cnt_n0 = 0
for c in C:
    if c == 0:
        cnt_0 += 1
    else:
        cnt_n0 += 1


if C[-1] == 0:
    ans_min = cnt_n0
    ans_max = cnt_n0
else:
    if sum(C) == C[-1]:
        ans_min = 1
    else:
        ans_min = cnt_n0 - 1

    ans_max = cnt_n0 - 1 + C[-1]


print(ans_min, ans_max)
