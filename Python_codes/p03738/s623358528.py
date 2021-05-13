A = input()
B = input()
dA = len(A)
dB = len(B)
if dA > dB:
    print("GREATER")
elif dA < dB:
    print("LESS")
else:
    judge = 1
    for i in range(dA):
        if int(A[i]) > int(B[i]):
            print("GREATER")
            judge = 0
            break
        elif int(A[i]) < int(B[i]):
            print("LESS")
            judge = 0
            break
    if judge == 1:
        print("EQUAL")