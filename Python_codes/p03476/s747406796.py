from itertools import accumulate

# エラトステネスの篩
def prime_eratosthenes(n):
    prime_list = []
    num_set = set()
    for i in range(2, n + 1):
        if i not in num_set:
            prime_list.append(i)
            for j in range(i * i, n + 1, i):
                num_set.add(j)
    return prime_list


l1 = set(prime_eratosthenes(10 ** 5))
l2 = set()
l3 = [0] * 10 ** 5

for i in l1:
    if (i + 1) // 2 in l1:
        l2.add(i)
for i in l2:
    l3[i] = 1

# 累積和
ans = list(accumulate(l3))


for i in range(int(input())):
    l, r = map(int, input().split())
    print(ans[r] - ans[l - 1])