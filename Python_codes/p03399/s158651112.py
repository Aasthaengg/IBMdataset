li1,li2 = [],[]
for i in range(4):
    if i <= 1:
        a = int(input())
        li1.append(a)
    else:
        a = int(input())
        li2.append(a)
print(min(li1)+min(li2))