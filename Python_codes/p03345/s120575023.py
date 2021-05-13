a,b,c,k=map(int,input().split())
if (a-b)!=0:
    if k%2==0:
        print(a-b)
    else:
        print((a-b)*-1)
else:
    print('0')