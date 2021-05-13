A = list(map(int,input().split()))
B = []

for i in range(0,3):
    for j in range(0,3):
        if j>i:
            temp = A[i] + A[j]
            B.append(temp)
            
if B[0] == A[2] or B[1] == A[1] or B[2] == A[0]:
    print('Yes')
else:
    print('No')