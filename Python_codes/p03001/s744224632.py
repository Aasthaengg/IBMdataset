if __name__=="__main__":
    w,h,x,y=[int(x) for x in input().split()]

    a=(w*h)/2

    print(a,end=' ')
    
    if x/1==w/2 and y/1==h/2:
        print(1)
    else: print(0)
