stak = []
for i in input().split():
    if i in "+-*":
        x = stak.pop()
        y = stak.pop()
        stak.append(str(eval(y + i + x)))
    else:
        stak.append(i)
print(stak.pop())
