import sys 

def func():
    n=int(input())
    print(0)
    sys.stdout.flush()
    gl=input()
    if gl == 'Vacant': 
        return
    print(n-1)
    sys.stdout.flush()
    gr=input()
    if gr == 'Vacant':
        return
    l=0
    r=n-1
    m=0
    while l<r-1:
        m=(l+r)>>1
        print(m)
        sys.stdout.flush()
        gm=input()
        if gm == 'Vacant' : 
            return  
        if (m-l)%2==0 and gm==gl :
            l=m
        elif (m-l)%2==1 and gm!=gl : 
            gl=gm
            l=m
        else :
            gr=gm
            r=m

    if m==l : 
        print(r)
        sys.stdout.flush()
    else: 
        print(l)
        sys.stdout.flush()
    return 

func()
