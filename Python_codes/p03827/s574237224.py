n = int(input())
S = list(input())
A = [0]
loop = 0
for e in S:
    A.append(A[loop] + 1) if e == 'I' else A.append(A[loop] - 1)
    loop += 1
print(max(A))
