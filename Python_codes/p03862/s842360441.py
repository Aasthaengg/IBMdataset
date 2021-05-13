# Beginner 50 C
N, x = map(int, input().split())
A = list(map(int, input().split()))
sum_s = sum(A)

for i in range(N-1):
    s = A[i] + A[i+1] - x
    if s > 0:
        A[i+1] = x - A[i]
        if A[i+1] >= 0:
            pass
        else:
            A[i] = A[i] + A[i+1]
            A[i+1] = 0
    else:
        pass

sum_e = sum(A)
print(sum_s - sum_e)
