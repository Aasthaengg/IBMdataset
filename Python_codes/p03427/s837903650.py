n = input()
A = []
sum = 0
for i in n:
    A.append(i)
    sum += int(i)

if A[0] == '1':
    print(max(sum, (len(A) - 1) * 9))
else:
    print(max(sum, (len(A) - 1) * 9 + int(A[0]) - 1))