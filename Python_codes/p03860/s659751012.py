def abc048():
    d=[]
    a=input()
    b=a.split()
    c=[i for i in b]
    k=''.join(c)
    for i in k:
        d.append(i)

    print(d[0],end='')
    print(d[len(c[0])],end='')
    print('C',end='')
    


abc048()
