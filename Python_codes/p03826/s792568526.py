a,b,c,d = map(int,input().split())

kekka1 = a*b
kekka2 = c*d

if kekka1 == kekka2:
    print(int(kekka1))
elif kekka1 > kekka2:
    print(int(kekka1))
else:
    print(int(kekka2))