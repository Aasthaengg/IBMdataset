#059_C
n=int(input())
a=list(map(int,input().split()))

def search(x):#x=0,1
    tmp=0
    cnt=0
    for i in range(n):
        tmp+=a[i]
        if i%2==x:
            if tmp<=0:
                cnt+=1-tmp
                tmp=1              
        else:
            if tmp>=0:
                cnt+=tmp+1
                tmp=-1
    return cnt

print(min(search(0),search(1)))