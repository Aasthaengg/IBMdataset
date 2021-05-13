from itertools import accumulate

n,m,k=map(int,input().split())
a_acum=list(accumulate(list(map(int,input().split()))))
b_acum=list(accumulate(list(map(int,input().split()))))

def ask_number(data,value):
    start,end=0,len(data)
    while True:
        mid=(start+end)//2
        if start == mid:
            break
        if data[mid] > value:
            end=mid
        else:
            start=mid
    if start == 0 and data[0] > value:
        return 0
    else:
        return end
    
ans=ask_number(b_acum,k)

for i in range(n):
        sub = k - a_acum[i]
        if sub < 0:
            break
        else:
            ans=max(ans,ask_number(b_acum,sub)+i+1)
print(ans)