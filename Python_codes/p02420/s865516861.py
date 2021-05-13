while 1:
    s=input()
    if s=="-" : break
    m=int(input())
    for _ in range(m):
        x=int(input())
        s=s[x:]+s[:x]
    print(s)
