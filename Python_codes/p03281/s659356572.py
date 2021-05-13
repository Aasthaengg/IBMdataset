N = int(input())

A = [0]*(N+1)
for i in range(1, N+1):
    for j in range(i, N+1, i):
        A[j] += 1

count = 0
for i in range(1, N+1):
    if i%2 == 1 and A[i] == 8:
        count += 1
print(count)