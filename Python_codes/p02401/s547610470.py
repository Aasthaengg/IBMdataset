def simple_calc(a, op, b):
    res = 0
    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        res = a// b

    return  res

if __name__ == "__main__":
    while True:
        a, op, b = input().split()
        if op == "?":
            break
        ans = simple_calc(int(a), op, int(b))
        print(f"{ans}")
        
    
