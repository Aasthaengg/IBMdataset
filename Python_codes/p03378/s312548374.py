N, M, X = map(int, input().split())
A = list(map(int, input().split()))
costRight, costLeft = 0, 0
for i in range(X, N):
    if i in A:
        costRight +=1
for i in range(X, 0, -1):
    if i in A:
        costLeft += 1
print(min(costRight, costLeft))