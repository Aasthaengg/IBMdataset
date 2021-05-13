from collections import deque

N, P = [int(x) for x in input().split()]

even = 0
odd = 0

for a in input().split():
    check = int(a)

    if check % 2 == 0:
        even += 1
    else:
        odd += 1


def comb(n, r):
    up = 1
    down = 1
    for i in range(r):
        up *= n - i
        down *= i + 1
    return up // down


# 奇数にする場合
result = 0
if P == 1:
    # 奇数を奇数個選ぶ
    for i in range(1, odd+1, 2):
        result += comb(odd, i)

# 偶数にする場合
else:
    # 奇数を選ばない、もしくは偶数個選ぶ
    for i in range(0, odd+1, 2):
        result += comb(odd, i)

if even == 0:
    mul = 1
else:
    mul = 2 ** even

result *= mul
print(result)
