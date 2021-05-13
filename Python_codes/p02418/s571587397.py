x = list(input())
y = list(input())
for a in range(len(y)):
    x.append(x[a])

i = 0
j = 0
while True :
    if y[j] == x[i]:
        j += 1
        if j == len(y):
            print("Yes")
            break
        i += 1
        if i == len(x):
            print("No")
            break
    else :
        i += (1 - j)
        if i == len(x):
            print("No")
            break
        j = 0
