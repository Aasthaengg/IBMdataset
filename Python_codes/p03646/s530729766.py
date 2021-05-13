k = int(input())
rem = k%50
quo = k//50

N = 50
A = [49+quo]*N

for i in range(50):
    if i < rem:
        A[i] += 50-(rem-1)
    else:
        A[i] -= rem

print(N)
print(*A)