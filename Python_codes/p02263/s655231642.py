#16D8103014C 安藤 陸人
#3_A
x = input().split()
flag = 0
j = -1
y = []
for i in range(len(x)):
    j = len(y) -1
    if x[i] == "+":
        a = y.pop(j)
        b = y.pop(j-1)
        y.append(b+a)
    elif  x[i] == "-":
        a = y.pop(j)
        b = y.pop(j-1)
        y.append(b-a)
    elif x[i] == "*":
        a = y.pop(j)
        b = y.pop(j-1)
        y.append(b*a)
    else:
        y.append(int(x[i]))
print(y[0])
