#import math
#from decimal import Decimal
import numpy as np
# nの約数を全て求める
# n!が大きすぎ＞　解説をみると。。
# ex; 24 = 2^3 * 3
#       (1,2,3,4,6,8,12,24) > 8個

# approach, 1~Nごとに、素因数分解をして、カウントする。
# 最後に掛け合わせる。
lim = 10 ** 9 + 7
n = int(input())
# https://note.nkmk.me/python-prime-factorization/

num = [0] * (n + 1)
#num[1] = 1

for i in range(2, n + 1):
    temp = i
    # even number
    while (temp % 2 == 0):
        if (num[2] == 0):
            num[2] = 1
        num[2] += 1
        # print('2A')
        temp //= 2

    f = 3
    # odd number
    while (f * f <= temp):
        if (temp % f == 0):
            if (num[f] == 0):
                num[f] = 1
            num[f] += 1
            #print('B', f)
            temp //= f
        else:
            f += 2
    # prime number
    if (temp != 1):
        if (num[temp] == 0):
            num[temp] += 1
        num[temp] += 1
        #print('C', temp)

numA = np.array(num)
numAA = np.argwhere(numA != 0)
numAAA = numAA.tolist()
# print(numA)

ans = 1
for i in numAAA:
    tar = i[0]
    ans *= num[tar]

#ans = sum(num)
ans %= lim

print(ans)
