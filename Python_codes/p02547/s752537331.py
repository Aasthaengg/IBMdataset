c=0
for _ in range(int(input())):
    x,y = map(int,input().split())

    if x==y:
        c+=1
    else:
        c=0
    if c==3:
        c=-1
        print('Yes')
        break
if c!=-1:
    print('No')
