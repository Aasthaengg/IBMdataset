x = list(input().split())
arr = []
for i in range(len(x)):
    if x[i] == '+':
        a = arr.pop()
        b = arr.pop()
        arr.append(a+b)
    elif x[i] == '-':
        b = arr.pop()
        a = arr.pop()
        arr.append(a-b)
    elif x[i] == '*':
        a = arr.pop()
        b = arr.pop()
        arr.append(a*b)
    else:
        arr.append(int(x[i]))
print(arr[-1])