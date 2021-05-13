# -*- coding: utf-8 -*-
N, T = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

max_diff = 0
max_value = A[-1]
for i in range(N-2, -1, -1):
    if A[i] > max_value:
        max_value = A[i]
        buf = [i]
    elif A[i] == max_value:
        pass
    else:
        max_diff = max(max_diff, max_value - A[i])


indices = set()
buf = [N-1]
max_value = A[-1]
for i in range(N-2, -1, -1):
    if A[i] > max_value:
        max_value = A[i]
        buf = [i]
    elif A[i] == max_value:
        pass
    else:
        if max_value - A[i] == max_diff:
            indices.add(i)

# print(indices)
print(len(indices))
