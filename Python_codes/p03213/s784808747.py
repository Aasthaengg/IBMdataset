#114_D
N=int(input())
prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

def Count(x):
    res=0
    tmp=N
    while tmp//x:
        tmp=tmp//x
        res+=tmp
    return res

cnt=[Count(p) for p in prime]

def Sum(n):
    return sum([x>=n for x in cnt])

Ans=0
Ans=Sum(74)+Sum(24)*(Sum(2)-1)+Sum(14)*(Sum(4)-1)+Sum(4)*(Sum(4)-1)*(Sum(2)-2)//2
print(Ans)