a = []
while True:
    x = map(str, raw_input().split())
    if x[1] == '?':
        break
    if x[1] == '+':
        a.append(int(x[0]) + int(x[2]))
    if x[1] == '-':
        a.append(int(x[0]) - int(x[2]))
    if x[1] == '*':
        a.append(int(x[0]) * int(x[2]))
    if x[1] == '/':
        a.append(int(x[0]) / int(x[2]))
for i in range(len(a)):
    print a[i]