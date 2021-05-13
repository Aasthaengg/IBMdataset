while True:
    s=input()
    if s=='-':
        break
    m=int(input())
    s=list(s)
    for i in range(m):
        h=int(input())
        for j in range(h):
            pop=s.pop(0)
            s.append(pop)
    a=''.join(s)
    print(a)
