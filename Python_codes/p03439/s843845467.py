n = int(input())
print(0)
s = input()
if s == "Vacant":
    exit()
elif s == "Male":
    print(n-1)
    s = input()
    if s == "Vacant":
        exit()
    else:
        l = 0
        r = n-1
        while True:
            m = (l+r)//2
            print(m)
            s = input()
            if s == "Vacant":
                exit()
            if m % 2 == 0 and s == "Male":
                l = m
            elif m % 2 == 1 and s == "Female":
                l = m
            else:
                r = m
elif s == "Female":
    print(n-1)
    s = input()
    if s == "Vacant":
        exit()
    else:
        l = 0
        r = n-1
        while True:
            m = (l+r)//2
            print(m)
            s = input()
            if s == "Vacant":
                exit()
            if m % 2 == 0 and s == "Male":
                r = m
            elif m % 2 == 1 and s == "Female":
                r = m
            else:
                l = m
