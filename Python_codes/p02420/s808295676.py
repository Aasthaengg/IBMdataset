while 1:
    w=raw_input()
    if w=='-':break
    n=input()
    for i in range(n):
        x=input()
        w=w[x:]+w[:x]
    print w
