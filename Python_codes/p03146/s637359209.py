s=int(input())
se={s}
for i in range(10000000):
    if s%2==0:
        s=s//2
        if s in se:
            print(i+2)
            exit()
        else:
            se.add(s)
    else:
        s=s*3+1
        if s in se:
            print(i+2)
            exit()
        else:
            se.add(s)