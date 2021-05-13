from sys import stdin

while True:
    a, op, b = stdin.readline().rstrip().split()
    if op == "+":
        print(int(a)+int(b))
    elif op == "-":
        print(int(a)-int(b))
    elif op == "*":
        print(int(a)*int(b))
    elif op == "/":
        print(int(a)//int(b))
    else: # op == "?"
        break

