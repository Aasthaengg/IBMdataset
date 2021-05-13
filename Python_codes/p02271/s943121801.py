from itertools import product

n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

A = [0]*(2**n)
c = 0
for x in product([0,1], repeat=n):
    summ = 0
    for j in range(n):
        if x[j] == 1:
            summ += a[j]
    A[c] = summ
    c+=1

for i in range(q):
    if m[i] in A:
        print('yes')
    else:
        print('no')
