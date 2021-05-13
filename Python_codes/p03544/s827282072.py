N = int(input())
L = [2,1]+[0]*100
for i in range(2,100):
    L[i] = L[i-1]+L[i-2]
print(L[N])