N = int(input())
MAX = 86
L = [0]*(MAX+1)
L[0] = 2
L[1] = 1
for i in range(2, MAX+1):
    L[i] = L[i-1] + L[i-2]
print(L[N])