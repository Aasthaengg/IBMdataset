N, x = map(int, input().split())
A = [int(i) for i in input().split()]

A = sorted(A)

i = 0
while i < N:
    if A[i] <= x:
        x -= A[i]
        i += 1
    else:
        break

if i == N and x > 0:
    i -= 1

print(i)
