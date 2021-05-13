s = []
for i in input().split():
    if i in ('+', '-', '*'):
        s.append(eval(str(s.pop(-2)) + i + str(s.pop(-1))))
    else:
        s.append(i)
print(s.pop())

