n=int(input())
p=int((2*n)**0.5)
if n!=((p+1)*p)//2:
    print("No")
else:
    t=[[]for i in range(p+1)]
    c=1
    for i in range(1,p+1):
        for j in range(i):
            t[i].append(c)
            t[j].append(c)
            c+=1
    print("Yes")
    print(p+1)
    for i in t:
        i=[len(i)]+i
        print(*i)