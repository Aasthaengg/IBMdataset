w=input()
lst=[]
flag = 0
for i in w:
    lst.append(i)

for i in range(len(w)):
    if lst[i] == 99:
        continue
    c = 1
    j = i + 1
    while j < len(w):
        if lst[i] == lst[j]:
            lst[j] = 99
            c += 1
        j += 1
    if c % 2 != 0:
        print("No")
        flag = 1
        break

if flag == 0:
    print("Yes")
