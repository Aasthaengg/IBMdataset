def judgetest(a, b, c):
    if a == -1 or b == -1:
        return 'F'
    sum = a + b
    if sum >= 80:
        return 'A'
    elif sum >= 65:
        return 'B'
    elif sum >= 50:
        return 'C'
    elif sum >= 30:
        if c >= 50:
            return 'C'
        else:
            return 'D'
    else:
        return 'F'

list = []
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    list.append(judgetest(a, b, c))

for s in list:
    print(s)