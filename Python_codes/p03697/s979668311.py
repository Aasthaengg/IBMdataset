A_B = str(input())
A = int(A_B.split(" ")[0])
B = int(A_B.split(" ")[1])

if (A + B >= 10):
    print("error")
else:
    print(A + B)
