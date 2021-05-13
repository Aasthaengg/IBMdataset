A = list(map(int, list(input())))

for i in range(1 << 3):
    x = A[0]
    ans = str(A[0])
    for j in range(3):
        if i & 1 << j > 0:
            x += A[j + 1]
            ans += '+' + str(A[j + 1])
        else:
            x -= A[j + 1]
            ans += '-' + str(A[j + 1])
    if x == 7:
        print(ans + "=7")
        break
            
