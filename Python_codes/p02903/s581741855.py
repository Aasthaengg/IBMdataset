h,w,a,b=map(int,input().split())
plus=[0 if i<a else 1 for i in range(w)]
minus=[1 if i<a else 0 for i in range(w)]

for i in range(h):
    if i<b:
        print(*plus,sep="")
    else:
        print(*minus,sep="")