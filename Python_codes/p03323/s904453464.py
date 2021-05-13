line = input()
A, B = [int(n) for n in line.split()]
if A > 8 or B > 8:
    print(":(")
else:
    print("Yay!")