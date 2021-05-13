import copy

N = int(input())
A = [int(input()) for _ in range(N)]

first = 0
second = 0

aa = copy.deepcopy(A)
aa.sort()

for a in aa:
    if a >= first:
        second = first
        first = a

for a in A:
    if a == first:
        print(second)
    else:
        print(first)
