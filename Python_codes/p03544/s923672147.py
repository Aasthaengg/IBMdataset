N = int(input())

L = [2, 1]

for i in range(2, N+1):
    L_i = L[i-1] + L[i-2]
    L.append(L_i)

print(L[-1])