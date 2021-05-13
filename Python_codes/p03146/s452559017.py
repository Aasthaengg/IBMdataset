s = int(input())

a = []
i = 0
while 1:
    if i==0:
        nexta = s
    else:
        if a[-1]%2==0:
            nexta = a[-1]//2
        else:
            nexta = 3*a[-1]+1
    i += 1
    if nexta in a:
        break
    a.append(nexta)
print(i)
