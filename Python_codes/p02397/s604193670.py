while(1):
    a,b = [int(i) for i in input().split()]
    if a == 0 and b == 0:
        break
    c = [a,b]
    c.sort()
    print(*c,sep=" ")
