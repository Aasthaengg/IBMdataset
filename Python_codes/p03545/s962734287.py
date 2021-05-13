A = list(map(int, list(input())))

for i in range(2 ** 3):
    ans = A[0]
    op = []
    for j in range(3):
        if ((i >> j) & 1):
            ans += A[j + 1] 
            op.append("+")
        else:
            ans -= A[j + 1]
            op.append("-")
    if ans == 7:
        break
A = list(map(str, A))
print(A[0], end="")
for c in range(3):
    print(op[c], end="")
    print(A[c + 1], end="")
print("=7")