X, Y, Z, k = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
C = list(int(x) for x in input().split())

AB = []
for x in range(X):
    for y in range(Y):
        AB.append(A[x] + B[y])
AB.sort(reverse=True)
C.sort(reverse=True)

ANS = []
for i in range(min(k, X * Y)):
    for z in range(Z):
        ANS.append(AB[i] + C[z])
ANS.sort(reverse=True)

for ans in ANS[:k]:
    print(ans)
