while 1:
    n=input()
    if n=='-':
        break
    m=[i for i in range(len(n))]
    count=int(input())
    for i in range(count):
        l=int(input())
        for j in range(len(n)):
            m[j]=n[(l+j)%len(n)]
        n=m.copy()
    for i in range(len(n)):
        print(n[i],end="")
    print()     