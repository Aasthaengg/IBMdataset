d = {}
while 1:
    try:
        se = input().lower()
    except:
        break
    for i in se:
        if i.isalpha():
            d[i] = d.get(i, 0) + 1
for i in 'abcdefghijklmnopqrstuvwxyz':
    d[i] = d.get(i, 0)
    print("{} : {}".format(i, d[i]))
