A_B_C = list(map(int, input().split()))
A_B_C.sort()
print(int(str(A_B_C[2]) + str(A_B_C[1])) + A_B_C[0])
