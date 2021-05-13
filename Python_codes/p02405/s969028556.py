while 1:
    h,w=map(int,input().split())
    if h==0: break
    for i in range(h):
        for j in range(w):
            print('#.'[(i+j)&1],end='')
        print()
    print()

