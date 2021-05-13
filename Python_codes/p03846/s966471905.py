import collections

n = int(input())
lst = [int(s) for s in input().split()]

is_success = True

if n % 2 == 1:
    is_success = lst.count(0) == 1

counters = collections.Counter(lst)

for i in range(n - 1, 0, -2):
    if counters[i] != 2:
        is_success = False
        break

if is_success:
    tmp = 1

    for _ in range(n // 2):
        tmp *= 2
        tmp %= 10 ** 9 + 7

    print(tmp)
else:
    print(0)
