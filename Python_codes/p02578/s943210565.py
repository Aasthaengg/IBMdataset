N = int(input())
A = list(map(int, input().split()))

i = 0
step = []
while i <= len(A) - 2:
    if A[i] > A[i+1]:
        step.append(A[i] - A[i+1])
        A[i+1] = A[i]
        i += 1
    else:
        i += 1

print(sum(step))
