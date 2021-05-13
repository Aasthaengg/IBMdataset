#coding:utf-8

moji = list(input().rstrip())
moji2 =[]
for i in moji:
    if i.isalpha() == False:
        moji2.append(i)

    elif i.islower() == True:
        moji2.append(i.upper())
    else:
        moji2.append(i.lower())

print("".join(moji2))