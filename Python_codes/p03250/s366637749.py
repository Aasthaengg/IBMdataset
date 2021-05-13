arrtemp = []

A, B, C = map(int,input().split())
arrtemp.append(A)
arrtemp.append(B)
arrtemp.append(C)

print(max(arrtemp)*10+sorted(arrtemp)[1]+min(arrtemp))