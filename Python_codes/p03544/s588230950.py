N = int(input())
L = []
L.append(2)
L.append(1)

for i in range(2,N+1):
    L_temp = L[i-1] + L[i-2]
    L.append(L_temp)

print(L[-1])