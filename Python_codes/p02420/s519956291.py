while True:
    t=str(input())
    if t=="-":
        break
    m=int(input())
    a=0
    while a<m:
        b=int(input())
        t=t[b:]+t[:b]
        a+=1
    print(t)
