n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
combi = set()

for i in range(1<<n):
    total = 0
    for j in range(n):
        if (i >> j) & 1:
            total += A[j]
    combi.add(total)

for num in m:
    if num in combi:
        print('yes')
    else:
        print('no')

