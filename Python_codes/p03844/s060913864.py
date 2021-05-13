# AtCoder Beginner Contest 050
# A - Addition and Subtraction Easy
l = input().split()
A = int(l[0])
op = str(l[1])
B = int(l[2])
if op == '+':
    print(A+B)
elif op == '-':
    print(A-B)