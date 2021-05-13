s = int(input())
if 10**9 >= s:
    print(0,0,s,0,0,1)
    exit()
x = int(s**0.5)
if x**2 >= s:
    t = x**2-s
    if t <= 10**9:
        print(0,0,x,1,t,x)
else:
    if x*(x+1) >= s:
        t = x*(x+1) -s
        if t <= 10**9:
            print(0,0,x,1,t,x+1)
    elif (x+1)**2 >= s:
        t = (x+1)**2 - s
        if t <= 10**9:
            print(0,0,x+1,1,t,x+1)
