from collections import Counter
s = input()
dic = dict(Counter(s))
if len(dic)==1:
    for v in dic.values():
        if v==1:
            print('YES')
        else:
            print('NO')
elif len(dic)==2:
    for v in dic.values():
        if v>=2:
            print('NO')
            break
    else:
        print('YES')
else:
    a = dic['a']
    b = dic['b']
    c = dic['c']
    if a==b==c:
        print('YES')
    elif a==b and abs(b-c)<=1:
        print('YES')
    elif b==c and abs(c-a)<=1:
        print('YES')
    elif c==a and abs(a-b)<=1:
        print('YES')
    else:
        print('NO')