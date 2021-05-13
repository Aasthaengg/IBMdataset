a,b,k=map(int, input().split())

if k<a:
    a-=k
    print(a,b,sep=" ")
else:
    k-=a
    b-=k
    if 0<=b:
        print(0,b,sep=" ")
    else:
        print(0,0,sep=" ")