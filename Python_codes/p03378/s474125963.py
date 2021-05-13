N, M, X = map(int, input().split())
A = list(map(int, input().split()))
costRight, costLeft = 0, 0
for a in A:
    if a > X:
        costRight += 1
    else:
        costLeft +=1
print(min(costLeft, costRight))