N=int(input())
L=[2,1]
for i in range(N):
    L.append(L[len(L)-1]+L[len(L)-2])
print(L[len(L)-2])