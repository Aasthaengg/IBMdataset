data = input().split(" ");

def reverse_polish_notation(data):
    operands = [];
    for n in data:
        if n not in "*+-":
            operands.append(int(n));
        else:
            operand_second = operands.pop();
            operand_first = operands.pop();
            operands.append(calculate(n, operand_first, operand_second));
    return operands[0];

def calculate(operator, a, b):
    if operator == "*":
        return a * b;
    elif operator == "-":
        return a - b;
    elif operator == "+":
        return a + b;

print(reverse_polish_notation(data));
