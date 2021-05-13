N = int(input())
L = [2, 1]

for i in range(1, N):
    L += [L[-1] + L[-2]]
print(L[N])