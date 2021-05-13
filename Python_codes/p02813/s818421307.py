import itertools

N = int(input())
P = list(map(int, input().split()))
tuple_P = tuple(P)
sorted_P = sorted(P)
Q = list(map(int, input().split()))
tuple_Q = tuple(Q)
sorted_Q = sorted(Q)

count_P = 1
for perm_P in itertools.permutations(sorted_P):
    if tuple_P == perm_P:
        break
    count_P += 1

count_Q = 1
for perm_Q in itertools.permutations(sorted_Q):
    if tuple_Q == perm_Q:
        break
    count_Q += 1

answer = abs(count_P - count_Q)
print(answer)