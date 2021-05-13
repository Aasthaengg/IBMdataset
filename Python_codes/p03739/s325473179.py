import copy 

def resolve(List):
    # L[0]!=0を起点とする
    L = copy.deepcopy(List)
    cnt = 0
    s = L[0]
    for i in range(1,len(L)):
        a = L[i]
        if(s>0 and s+a>=0):
            L[i] = -s-1
            cnt += (s+a+1)
            s = -1
        elif(s<0 and s+a<=0):
            L[i] = -s+1
            cnt += (-s-a+1)
            s = 1
        else:
            s += a
    return cnt      

def ans(List):
    L = copy.deepcopy(List)
    a = L[0]
    c0,c1=0,0

    if (a>0):
        c0 = resolve(L)
        c1 = (a+1) + resolve([-1]+L[1:])
    elif (a<0):
        c0 = resolve(L)
        c1 = (-a+1) + resolve([1]+L[1:])
    else:
        c0 = 1 + resolve([1]+L[1:])
        c1 = 1 + resolve([-1]+L[1:])
    
    return(min(c0,c1))

N = int(input())
List = [int(x) for x in input().split(' ')]
print(ans(List))
