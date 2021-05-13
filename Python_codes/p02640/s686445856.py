x,y = map(int,input().split())

l = []
c = 2 * x
l.append(c)
for nn in range(x):
    c += 2
    l.append(c)

flag = False
for ll in l:
    if ll == y:
        print("Yes")
        flag = False
        break

    else:
        flag = True

if flag:
    print("No")