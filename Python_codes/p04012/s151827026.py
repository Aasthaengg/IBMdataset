w = list(input())
w.sort()
c = 0
flag = 0
if len(w) % 2 == 0:
    for i in range(round(len(w) / 2)):
        if w[c] != w[c + 1]:
            flag = 1
            break
        c += 2
    if flag == 1:
        print("No")
    else:
        print("Yes")
else:
    print("No")