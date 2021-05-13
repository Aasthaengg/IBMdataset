A = input()
B = input()

pw = ""
if len(A) == len(B):
    for i in range(len(A)):
        pw += A[i]
        pw += B[i]
    print(pw)
    exit()

else:
    for i in range(len(B)):
        pw += A[i]
        pw += B[i]
    print(pw + A[-1])
    exit()