h,w,a,b=map(int,input().split())
flag=0
for i in range(h):
    if 0<=i<b: flag=1
    else: flag=0
    for j in range(w):
        if flag:
            if 0<=j<a: print(0,end="")
            else: print(1,end="")
        else:
            if 0<=j<a: print(1,end="")
            else: print(0,end="")
    print()