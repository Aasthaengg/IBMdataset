n,a,b = [int(x) for x in input().split()]

t = 1
while True:
    if t==1:#Alice
        if a+1==b:
            if a==1:
                print("Borys")
                break
            else:
                a -= 1
        else:
            a += 1
    else:
        if b-1==a:
            if b==n:
                print("Alice")
                break
            else:
                b += 1
        else:
            b -= 1
    t += 1
    t %= 2