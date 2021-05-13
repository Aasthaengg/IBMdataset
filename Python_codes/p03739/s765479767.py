n = int(input())
A = list(map(int,input().split()))

CumSum = [0] * n
c = 0
for i,a in enumerate(A):
    c += a
    CumSum[i] = c
# 最初が正の場合
total_cost = 0
c_sum = 0
for i,a in enumerate(A):
    c_sum += a
    if i % 2 ==0:
        if c_sum > 0:
            continue
        total_cost += abs(c_sum)+ 1
        c_sum = 1
        continue

    if c_sum < 0:
        continue
    total_cost += abs(c_sum)+ 1
    c_sum = -1
# 最初が負の場合
total_cost2 = 0
c_sum = 0
for i,a in enumerate(A):
    c_sum += a
    if i % 2 ==0:
        if c_sum < 0:
            continue
        total_cost2 += abs(c_sum)+ 1
        c_sum = -1
        continue

    if c_sum > 0:
        continue
    total_cost2 += abs(c_sum)+ 1
    c_sum = 1
print(min(total_cost,total_cost2))

