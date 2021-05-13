s = list(input())
x, y = map(int, input().split())

X = [0]
Y = [0]

flag = True
tmp = 0
for i in s:
    if i == 'F':
        tmp += 1
    else:
        if flag:
            X.append(tmp)
        else:
            Y.append(tmp)
        tmp = 0
        flag = not flag

if flag:
    X.append(tmp)
else:
    Y.append(tmp)

# print (X)
# print (Y)

x -= X[1]
X[1] = 0

x = abs(x)
y = abs(y)

total_X = sum(X)
total_Y = sum(Y)

lst_X = [0] * (total_X + 1)
lst_X[0] = 1
for i in X:
    if i == 0:
        continue
    for j in range(total_X - i, -1, -1):
        if lst_X[j] == 1:
            lst_X[j + i] = 1

# print (lst_X)

lst_Y = [0] * (total_Y + 1)
lst_Y[0] = 1
for i in Y:
    if i == 0:
        continue
    for j in range(total_Y - i, -1, -1):
        if lst_Y[j] == 1:
            lst_Y[j + i] = 1

# print (lst_Y)
if x > total_X or y > total_Y:
    print ('No')
    exit()

if (total_X - x) % 2 == (total_Y - y) % 2 == 0 and lst_X[(total_X - x) // 2] == 1 and lst_Y[(total_Y - y) // 2]:
    print ('Yes')
else:
    print ('No')