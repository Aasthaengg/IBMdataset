buf = []
while True:
    in_line = raw_input().split()
    if in_line[1] == "?":
        break
    else:
        a = int(in_line[0])
        b = int(in_line[2])
        op = in_line[1]
        if op == "+":
            buf.append(a+b)
        elif op == "-":
            buf.append(a-b)
        elif op == "*":
            buf.append(a*b)
        elif op == "/":
            buf.append(a/b)
for i in buf:
    print i