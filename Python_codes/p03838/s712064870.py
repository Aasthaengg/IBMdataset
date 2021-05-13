x,y=map(int,input().split())
if x==y:
    print(0)
    exit()
def solve(x,y):
    if x>=0 and y>=0:
        if x<=y:
            return y-x
        elif y==0:
            return x+1
        else:
            return x-y+2
    elif x<0 and y<0:
        if x>y:
            return x-y+2
        else:
            return y-x
    elif x>=0 and y<0:
        return x-y+1
    else:
        return y-x

if x*y>=0:
    print(solve(x,y))
else:
    print(min(solve(-x,y)+1,solve(x,-y)+1,solve(x,y)))