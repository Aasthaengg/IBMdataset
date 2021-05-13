N = int(input())
Plist = []
i=1
print(" ",end="")
while i <= N:
    k=1
    if i%3 == 0:
        Plist.append(i)
    elif i%10 == 3:
        Plist.append(i)
    else:
        while i//k>1 and k>=0:
            if i//k%10 == 3:
                Plist.append(i)
                break
            else:
                k = k*10
    i=i+1
print(' '.join(map(str,Plist)))