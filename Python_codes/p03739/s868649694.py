import sys

n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

S = [0 for _ in range(n)]
acum = 0
for i in range(n):
    acum += A[i]
    S[i] = acum
# print(S)

costs = [0, 0]
for p in (0, 1):
    S_tmp = S[:]
    cost = 0 # BA`:n2s?t
    diff = 0 # +-B$NA`:n$G$NJQF0
    for i in range(n):
        # nB$H0lCW$9$kJ}$rIi$K$9$k
        # print(p, diff + S_tmp[i])
        if i % 2 == p:
            if diff + S_tmp[i] >= 0:
                tmp_cost = diff + S_tmp[i] + 1
                diff -= tmp_cost
                cost += tmp_cost
                # print("cost", cost)
        else:
            # B@5$KJQ49$9$k%3%9%H
            if diff + S_tmp[i] <= 0:
                tmp_cost = 1 - diff - S_tmp[i]
                diff += tmp_cost # +1B$KJQ49$9$k
                cost += tmp_cost
                # print("cost", cost)
    costs[p] = cost

# print(costs)
print(min(costs))