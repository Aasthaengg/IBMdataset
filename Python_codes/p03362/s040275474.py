a=[2];b=[2]
for i in range(3,100000):
    t=0
    while t<len(a):
        if i%a[t]==0:
            break
        else:t+=1
    else:
        a.append(i)
        if i%5==2:
            b.append(i)

    if len(b)==55:
        break

b.sort()
print(*b[:int(input())])