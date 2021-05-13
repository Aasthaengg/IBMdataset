while True:
    n=input()
    if n=="-":
        break
    l=list(n)
    m=int(input())
    for i in range(m):
        h=int(input())
        l=l[h:len(n)]+l[0:h]
    print(''.join(l))
