n,w = map(int,input().split())
w1,v1 = map(int,input().split())
if n == 1:
    if w1 <= w:
        print(v1)
    else:
        print(0)
else:
    a = [v1] 
    b = []
    c = []
    d = []
    for i in range(n-1):
        p,q = map(int,input().split())
        if p == w1:
            a.append(q)
        elif p == w1 + 1:
            b.append(q)
        elif p == w1 + 2:
            c.append(q)
        else:
            d.append(q)
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    a = a[::-1]
    b = b[::-1]
    c = c[::-1]
    d = d[::-1]
    #print(a,b,c,d)
    jkl = 0
    ass = 0
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            for h in range(len(c)+1):
                for g in range(len(d)+1):
                    if w1*(i+j+h+g)+j+2*h+3*g <= w:
                        ans = sum(a[:i:]) + sum(b[:j:]) + sum(c[:h:]) + sum(d[:g:])
                        ass = max(ass,ans)
    print(ass)


