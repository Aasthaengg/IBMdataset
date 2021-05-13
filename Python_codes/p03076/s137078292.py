from itertools import permutations
dishes = [int(input()) for _ in range(5)]
res = 10 ** 3
for di in permutations(dishes):
    tmp = 0
    for d in di:
        if tmp % 10 != 0:
            tmp += (10 - tmp % 10)
        tmp += d
    res = min(res, tmp)
print(res)