# coding: utf-8

str = input()
table = list(str)
count = 0
if len(str) % 2 == 0:
    for i in range(len(str)):
        if table[i] == table[(len(str)-1)-i]:
            continue
        else:
            count += 1
elif len(str) % 2 == 1:
    for i in range(len(str)):
        if table[i] == table[(len(str)-1)-i]:
            continue
        else:
            count +=1
if count == 0:
    print(0)
else:
    print(int(count / 2))
