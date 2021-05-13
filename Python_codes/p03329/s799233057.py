n = int(input())
A = [1]+[pow(6,i) for i in range(1,7)]+[pow(9,i) for i in range(1,6)]
D = [0]+[-1]*n
for i in range(1,n+1):
    D[i] = D[i-1]+1
    for j in range(1,7):
        if pow(6,j)>i: break
        D[i] = min(D[i], D[i-pow(6,j)]+1)
    for j in range(1,6):
        if pow(9,j)>i: break
        D[i] = min(D[i], D[i-pow(9,j)]+1)
print(D[-1])