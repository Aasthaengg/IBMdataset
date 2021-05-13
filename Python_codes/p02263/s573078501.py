x = input().split()
A = []
for i in x:
    try:
        A.append(int(i))
    except:
        b = A.pop()
        a = A.pop()
        if i == '+':
            A.append(a + b)
        if i == '-':
            A.append(a - b)
        if i == '*':
            A.append(a * b)
print(A.pop())