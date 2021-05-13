def calc(a, b, op):
    if op == "+":
        return a + b;
    elif op == "-":
        return a - b;
    elif op == "*":
        return a * b;
    elif op == "/":
        return a / b;
    elif op == "?":
        return None;

while True:
    a, op, b = input().split()
    result = calc(int(a), int(b), op)
    if result is not None:
        print(int(result));
    else:
        break;