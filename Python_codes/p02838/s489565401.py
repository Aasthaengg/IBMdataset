N = int(input())
A = list(map(int, input().split()))
MOD = 1000000007

sum_all = 0
p = 1
for i in range(60):
    ones = 0
    zeros = 0

    x = 1 << i
    for a in A:
        if a & x:
            ones += 1
        else:
            zeros += 1

    sum_all += p * ones * zeros % MOD
    p *= 2 % MOD


print(sum_all % MOD)
