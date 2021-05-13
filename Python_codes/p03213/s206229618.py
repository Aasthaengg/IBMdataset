from collections import defaultdict

N = int(input())

dic = defaultdict(int)


def factoring(k): #kを因数分解し、素因数とその個数を辞書に入れて返す。
    import math
    n = int(math.sqrt(k))+2
    for i in range(2, n):
        count = 0
        while k%i == 0:
            count += 1
            k = k//i
        if count != 0:
            dic[i] += count
    if k != 1: #sqrt(k)までチェックしてもkが1になっていない --> kが素因数
        dic[k] += 1
    return

for i in range(1, N + 1):
    factoring(i)

ans = 0
for i in dic:
    if dic[i] >= 74:
        ans += 1
    if dic[i] >= 2:
        count = 0
        for j in dic:
            if i == j:
                continue
            if dic[j] >= 4:
                count += 1
        ans += count * (count - 1) // 2
    if dic[i] >= 2:
        for j in dic:
            if i == j:
                continue
            if dic[j] >= 24:
                ans += 1
    if dic[i] >= 4:
        for j in dic:
            if i == j:
                continue
            if dic[j] >= 14:
                ans += 1

print (ans)
# print (dic)