dataset = []
op = ""
while op is not "?":
    a, op, b = map(str, input().split())
    a = int(a)
    b = int(b)
    if (a >= 0 and a <= 20000) and (b >= 0 and b <= 20000):
        listed = []
        listed.append(a)
        listed.append(op)
        listed.append(b)
        dataset.append(listed)
    elif op is "?":
        break
    else:
        break

for i in dataset:
    if i[1] is "+":
        print("{0}".format(i[0] + i[2]))
    elif i[1] is "-":
        print("{0}".format(i[0] - i[2]))
    elif i[1] is "*":
        print("{0}".format(i[0] * i[2]))
    elif i[1] is "/":
        print("{0}".format(int(i[0] / i[2])))
    else:
        pass