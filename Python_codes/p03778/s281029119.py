W,a,b = list(map(int,input().split()))

if (a-W)<=b<=(a+W):
    print(0) 
elif a+W<b:
    print(b-a-W)
elif b+W<a:
    print(a-b-W)