while 1:
    s=input()
    if(s == '-'): break
    m=int(input())
    for _ in range(0,m):
        h=int(input())
        s = s[h:]+s[0:h]
    print(s)