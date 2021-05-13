from collections import defaultdict
N = int(input())
MOD = 10**9 + 7


def f(v):
    a = 2
    dic = defaultdict(int)
    while v != 1:
        if v % a == 0:
            dic[a] += 1
            v //= a
        else:
            a += 1
    return dic


if N == 1:
    print(1)
    exit()

dic = defaultdict(int)
for i in range(2, N + 1):
    d = f(i)
    for key, value in d.items():
        dic[key] += value

# print('dic', dic)
ans = 1
for value in dic.values():
    ans *= value + 1
    ans %= MOD
print(ans)
