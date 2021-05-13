L = []
for i in range(87):
    L.append(i)
n = int(input())
L[0] = 2
L[1] = 1

for j in range(2,n+1):
    L[j] = L[j-1] + L[j-2]
print(L[n])