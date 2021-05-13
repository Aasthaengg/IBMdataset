k = int(input())
A = [x for x in range(50)]

plus = k // 50
A_plus = [x + plus for x in A]

res = k % 50
for i in range(res):
    A_plus = sorted(A_plus)
    A_plus[0] = A_plus[0] + 50
    for j in range(1,50):
        A_plus[j] = A_plus[j] -1

print(50)
print(' '.join([str(x) for x in A_plus]))
