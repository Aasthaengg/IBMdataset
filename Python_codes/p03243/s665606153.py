n = input()
if n.count(n[0]) == 3:
    print(n)
else:
    num = int(str(n[0])+str(n[0])+str(n[0]))
    if int(n) > num:
        a = min(int(n[0])+1, 9)
        print("%d%d%d" % (a, a, a))
    else:
        print(num)
