# coding: utf-8
import itertools

N, M = list(map(int, input().split(" ")))
k = []
for _ in range(M):
    k.append(list(map(int, input().split(" "))))
p = list(map(int, input().split(" ")))

bits = itertools.product(["on", "off"], repeat=N)

def tento(bit, k, p):
    for i, pi in enumerate(p):
        ki = list(k[i])
        tmp = 0
        for kij in ki[1:]:
            if bit[kij-1] == "on":
                tmp += 1
        if tmp % 2 != pi:
            return False
    return True

res = 0
for bit in bits:
    if tento(bit, k, p):
        res+=1
print(res)