K = int(input())

A = [0 for _ in range(K)]
for i in range(K):
    if i == 0:
        mod = 7 % K
    else:
        mod = (10 * A[i-1] + 7) % K
    A[i] = mod
    if mod == 0:
        print(i+1)
        exit()
print(-1)
