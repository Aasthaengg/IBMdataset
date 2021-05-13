N = int(input())
L = [2, 1]
i = 1
while i < N:
    i += 1
    L[0], L[1] = L[1], L[0]+L[1]
print(L[1])
