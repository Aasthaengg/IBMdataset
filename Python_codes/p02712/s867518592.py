N = int(input())

A = list(range(1,N+1))

i = 1
while 3*i <= N:
    A[i * 3-1] = 0
    i += 1

i = 1
while 5*i <= N:
    A[i * 5-1] = 0
    i += 1

print(sum(A))