l = []
for i in range(6):
    l.append(int(input()))

flag = "Yay!"
for i in range(4):
    for j in range(i+1, 5):
        d = l[j]-l[i]
        # print(d)
        if d>l[-1]:
            flag = ":("
print(flag)
