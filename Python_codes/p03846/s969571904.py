from collections import Counter
import numpy as np

MOD = 10 ** 9 + 7

n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
# 0の個数は、count[0]
num = len(a)
ans = 1


if (num % 2 == 0):
    # 偶数パターン
    temp = 1
    loop = int(num / 2)
    for i in range(loop):
        tar = count[temp]
        if (tar == 2):
            ans *= 2
            temp += 2
        else:
            print(0)
            exit()

else:

    tar0 = count[0]
    if (tar0 == 1):
        pass
    else:
        print(0)
        exit()

    temp = 2

    for i in range(num // 2):
        if (count[temp] == 2):
            ans *= 2
            temp += 2
        else:
            print(0)
            exit()

ans %= MOD
print(ans)
