n = int(input())
A = []

for i in range(n):
    a = int(input())
    A.append(a)

A.sort()

odd = 0
prev = A[0]
cnt = 1

for i in range(1,n):
    if A[i] != prev:
        if cnt % 2 == 1:
            odd += 1
        cnt = 1
        prev = A[i]
    else:
        cnt += 1

if cnt % 2 == 1:
    odd += 1

print(odd)