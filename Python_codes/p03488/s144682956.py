import numpy as np
s = list(input())
x, y = map(int, input().split())

X = [0]
Y = [0]

X_append = X.append
Y_append = Y.append

flag = True
tmp = 0
for i in s:
    if i == 'F':
        tmp += 1
    else:
        if flag:
            X_append(tmp)
        else:
            Y_append(tmp)
        tmp = 0
        flag = not flag

if flag:
    X_append(tmp)
else:
    Y_append(tmp)

x -= X[1]
X[1] = 0

x = abs(x)
total_X = sum(X)

lst_X = np.zeros(total_X + 1, dtype = np.int32)
lst_X[0] = 1
for i in X:
    if i == 0:
        continue
    lst_X[i:] = np.maximum(lst_X[i:], lst_X[:-i])

if x > total_X or (total_X - x) % 2 == 1 or lst_X[(total_X - x) // 2] == 0:
    print ('No')
    exit()

y = abs(y)
total_Y = sum(Y)

lst_Y = np.zeros(total_Y + 1)
lst_Y[0] = 1
for i in Y:
    if i == 0:
        continue
    lst_Y[i:] = np.maximum(lst_Y[i:], lst_Y[:-i])

if  y <= total_Y and (total_Y - y) % 2 == 0 and int(lst_Y[(total_Y - y) // 2]) == 1:
    print ('Yes')
else:
    print ('No')