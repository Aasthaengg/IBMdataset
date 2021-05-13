def resolve():
    A, op, B = input().split()
    if op == "+":
        result = int(A) + int(B)
    elif op == "-":
        result = int(A) - int(B)
    print(result)

resolve()