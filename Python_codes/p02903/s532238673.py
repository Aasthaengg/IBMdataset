h,w,a,b=map(int,input().split())
for i in range(h):
    if i<=b-1:
        lists="0"*a+"1"*(w-a)
        print(lists)
    else:
        lists="1"*a+"0"*(w-a)
        print(lists)