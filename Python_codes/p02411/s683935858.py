for _ in range(10000):
    res = list(map(int,input().split()))
    if res == [-1,-1,-1]:
        break
    su = res[0]+res[1]
    if su<30:
        gr="F"
    elif su<50:
        if res[2]>=50:
            gr="C"
        else:
            gr="D"
    elif su<65:
        gr="C"
    elif su<80:
        gr="B"
    else:
        gr="A"
    if res[0]==-1 or res[1]==-1:
        gr="F"
    print(gr)

