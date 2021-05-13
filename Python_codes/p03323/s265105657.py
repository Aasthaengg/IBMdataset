A,B = input().split()

A = int(A)
B = int(B)

if A >= B:
    if A  <= 8:
        print("Yay!")
    else:
        print(":(")
else:
    if B  <= 8:
        print("Yay!")
    else:
        print(":(")
