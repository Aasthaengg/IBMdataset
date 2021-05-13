A = list(map(int, input().split()))
cost = 0
dif_1to2 = abs(A[0]-A[1])
dif_1to3 = abs(A[0]-A[2])
dif_2to3 = abs(A[1]-A[2])
dif = [dif_1to2,dif_1to3,dif_2to3]
print(sum(dif)-max(dif))