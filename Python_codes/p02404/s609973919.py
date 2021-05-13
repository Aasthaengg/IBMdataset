while 1:
    h,w=map(int,input().split())
    if h==0 and w==0: 
        break
    for y in range(h): 
        if y == 0 or y == h-1:
            print('#'*w)
        else: 
            print('#','.'*(w-2),'#',sep='')
    print('')

