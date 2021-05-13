#coding:utf-8


mo =""
moji_m =""

while True:
    try:
        mo = input().lower()
        moji_m += mo
    except:
        break


moji = list(moji_m.lower())
moji_l = list("abcdefghijklmnopqrstuvwxyz")
moji_c = [0 for i in range(26)]

for i in moji:
    #??¢??????????????????????????????
    if i.isalpha() == False:
        pass
    else:
        moji_c[moji_l.index(i)] += 1

for i in range(26):
    print(str(moji_l[i]) + " : " +str(moji_c[i]))