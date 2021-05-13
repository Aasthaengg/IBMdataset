h,w,a,b = map(int,input().split())

for i in range(h):
    if i<b:
        for k in range(a):
            print(1,end='')
        for l in range(w-a):
            print(0,end='')
        print()
    if i>=b:
        for k in range(a):
            print(0,end='')
        for l in range(w-a):
            print(1,end='')
        print()
