n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))
T = set()
for i in range(1, 2 ** n):
    total = 0
    for j in range(n):
        if i >> j & 1:
            total += A[j]
    T.add(total)
for m in M:
    if m in T:
        print('yes')
    else:
        print('no')
