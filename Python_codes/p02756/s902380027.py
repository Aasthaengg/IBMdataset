
s = input()

q = int(input())
x = []
y = []

flag = 0

for i in range(q):
    li = list(input().split())
    if flag%2 == 0:
        if li[0] == "2":
            if li[1] =="1":
                x.append(li[2])
            else:
                y.append(li[2])
        else:
            flag += 1

    else:
        if li[0] == "2":
            if li[1] =="1":
                y.append(li[2])
            else:
                x.append(li[2])
        else:
            flag += 1

if flag%2 == 0:
    x = x[::-1]
    print("".join(x)+s+"".join(y))

else:
    s = s[::-1]
    y = y[::-1]
    print("".join(y)+s+"".join(x))

