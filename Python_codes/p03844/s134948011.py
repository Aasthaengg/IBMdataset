AopB = input().split()
A = int(AopB[0])
B = int(AopB[2])

op = AopB[1]

if (op == "+"):
    print(A+B)
else:
    print(A-B)