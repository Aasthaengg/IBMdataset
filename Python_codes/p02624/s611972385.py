n=int(input())

bp = [0] * (n+10)
for i in range(2, n+10):
    if bp[i] == 0:
        bp[i] = i
        for j in range(i*i, n+1, i):
            if bp[j]==0:
                bp[j] = i


def f(k):
    if k==1:
        return 1
    z=[]
    p=bp[k]
    cnt=1
    ans=1

    while k>=2:
        k//=p
        if p==bp[k]:
            cnt+=1
        else:
#            print(" ",k,p)
            ans*=cnt+1
            cnt=1
            p=bp[k]

    return ans

ans=0
for i in range(1,n+1):
    #print(i,f(i))
    ans += i*f(i)

print(ans)