S = input()
A,B = S.split()

A = int(A)
B = int(B)

if A<=8 and B <=8:
    print("Yay!")
elif A>8 or B>8:
    print(":(")
