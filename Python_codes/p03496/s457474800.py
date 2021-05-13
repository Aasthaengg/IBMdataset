from itertools import chain, product

N = int(input())
a = list(map(int, input().split()))

a_abs_max = 0
for i in range(N):
    if a_abs_max < abs(a[i]):
        a_abs_max = abs(a[i])
        a_abs_max_index = i

result = []
if a_abs_max > 0:
    if a[a_abs_max_index] > 0:
        result = list(chain(iter([(a_abs_max_index + 1, a_abs_max_index + 1)]), product([a_abs_max_index + 1], range(1, N + 1)), map(lambda i: (i + 1, i + 2), range(N - 1)))) # 1-based indexing
    elif a[a_abs_max_index] < 0:
        result = list(chain(iter([(a_abs_max_index + 1, a_abs_max_index + 1)]), product([a_abs_max_index + 1], range(1, N + 1)), map(lambda i: (i + 1, i), range(N - 1, 0, -1)))) # 1-based indexing

print(len(result))
for x, y in result:
    print(x, y)