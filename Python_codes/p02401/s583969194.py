v = 0
i = 0
b = []
while v == 0:
    a = input().split()
    if a[1] == '+':
        b.append(int(a[0])+int(a[2]))
        i = int(i) + 1
    elif a[1] == '-':
        b.append(int(a[0])-int(a[2]))
        i = int(i) + 1
    elif a[1] == '*':
        b.append(int(a[0])*int(a[2]))
        i = int(i) + 1
    elif a[1] == '/':
        b.append(int(a[0])//int(a[2]))
        i = int(i) + 1
    else:
        v = 1

for j in range(int(i)):
    print(b[j])
