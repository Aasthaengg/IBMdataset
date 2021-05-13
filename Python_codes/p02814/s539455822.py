import functools
import sys

n, m = map(int, input().split())
a = list(map(lambda x: x // 2, map(int, input().split())))

# A[0]を素因数分解して2で割り切れる回数を数える
div = 0

a_0 = a[0]
while a_0 % 2 == 0:
    a_0 /= 2
    div += 1

# print("count = " + str(div))#

# Aのすべての整数がA[0]と同じ回数2で割り切れるか調べる
for i in range(1, len(a)):
    div2 = 0
    tmp_a = a[i]
    while tmp_a % 2 == 0:
        tmp_a /= 2
        div2 += 1
    # print("A[" + str(i) + "] count = " + str(div2))#
    if div2 != div:
        print("0")
        sys.exit()


def gcd(x, y):
    if x == 0:
        return y

    return gcd(y % x, x)


def least_common_multiple(iter):
    '''
    最小公倍数を返す
    '''
    lcm = lambda x, y: x * y // gcd(x, y)
    return functools.reduce(lcm, iter)


lc = least_common_multiple(a)
ans = 0
a = 1

ans = m // lc
if ans == 0:
    print(0)
    sys.exit()
if ans % 2 == 0:
    print(ans // 2)
else:
    print(ans // 2 + 1)
