N = int(input())

t=x=y=0

for _ in range(N):
    ti,xi,yi = map(int,input().split())
    T = ti-t
    X = xi-x
    Y = yi-y
    if ((T%2==0 and (X+Y)%2==0) or (T%2==1 and (X+Y)%2==1)) and T >= abs(X+Y):
        t=ti
        x=xi
        y=yi
    else:
        print('No')
        break
else:print('Yes')