def calc(a,op,b):
    if op == "+":
        r = a + b 
    if op == "-":
        r = a - b 
    if op == "*":
        r = a * b 
    if op == "/":
        r = a // b
    return r

if __name__ == '__main__':
    while True:
        a,op,b = input().split()
        if op == "?":
            break
        print(calc(int(a),op,int(b)))