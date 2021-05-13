N = int(input())
A = list(map(int,input().split()))
sumA = sum(A)

pL= 0
pR = sumA
cost = abs(pR - pL)
for i in range(N):
    pL += A[i]
    pR -= A[i]
    cost = min(cost, abs(pR - pL))
print(cost)

