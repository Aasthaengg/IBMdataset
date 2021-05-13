x,y=map(int,input().split())
a=[4, 6, 9, 11]
if x==2 and y==2:
    print('Yes')
else:
    if (x==2 and y!=2) or (x!=2 and y==2):
        print('No')
    elif x in a and y in a:
        print('Yes')
    elif not x in a and not y in a:
        print('Yes')
    else:
        print('No')