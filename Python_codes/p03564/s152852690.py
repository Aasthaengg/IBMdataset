from itertools import combinations_with_replacement

N = int(input())
K = int(input())


def times_two(n):
    return 2 * n


def plus_k(n):
    return n + K


ans = []
for funcs in combinations_with_replacement((times_two, plus_k), N):
    value = 1
    for func in funcs:
        value = func(value)
    ans.append(value)
print(min(ans))
