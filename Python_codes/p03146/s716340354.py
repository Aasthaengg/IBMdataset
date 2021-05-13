s = int(input())
a =[s]
i = 0
while True:
    i += 1
    if a[i-1] % 2 == 0:
        if (a[i-1]//2) in a:
            print(len(a)+1)
            break
        else:
            a.append(a[i-1]//2)
    elif a[i-1] % 2 == 1:
        if (a[i-1]*3+1) in a:
            print(len(a)+1)
            break
        else:
            a.append(a[i-1]*3+1)