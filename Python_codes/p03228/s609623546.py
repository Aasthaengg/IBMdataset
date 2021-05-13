A, B, K = map(int, input().split())
for i in range(K):
    if i % 2 == 0: 
        if A % 2 == 1:
            A -= 1
        temp1 = int(A / 2)
        A = A - temp1
        B = B + temp1
    else:
        if B % 2 == 1:
            B -= 1
        temp2 = int(B / 2)
        A = A + temp2
        B = B - temp2
print(A, B)