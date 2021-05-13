while True:
    sen = input()
    if sen == '-':
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        s1 = sen[0:h]
        s2 = sen[h:]
        sen = s2 + s1
    print(sen)