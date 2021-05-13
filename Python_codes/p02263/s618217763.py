operands = ["+","-","*"]
symbols = raw_input().split()
ans = 0
i = 0
while True:
    if len(symbols) == 1:
        break
    if symbols[i] in operands:
        a = int(symbols.pop(i-2))
        b = int(symbols.pop(i-2))
        o = symbols.pop(i-2)
        if o == "*":
            symbols.insert(i-2,a*b)
        elif o == "+":
            symbols.insert(i-2,a+b)
        elif o == "-":
            symbols.insert(i-2,a-b)
        else:
            "This operand is invalid."
            break
        i-=1
    else:
        i+=1
print symbols[0]