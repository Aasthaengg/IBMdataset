if __name__ == "__main__":

    while True:
        s = raw_input().split()
        a = int(s[0])
        b = int(s[2])
        op = s[1];

        if op == "*":
            x = a * b
        elif op == "+":
            x = a + b
        elif op == "-":
            x = a - b
        elif op == "/":
            x = a / b
        elif op == "?":
            break;
        print x