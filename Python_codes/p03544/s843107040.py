n = int(input())
MAX = 87
L = [0]*MAX
L[0] = 2
L[1] = 1
for i in range(2,MAX):
    L[i] = L[i-1]+L[i-2]

print(L[n])