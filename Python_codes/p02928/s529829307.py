n,k = map(int,input().split())
A=[int(i) for i in input().split()]
MOD = 10**9 + 7

def tent(a):
    t = len(a)
    res = 0
    for i in range(t-1):
        for j in range(i+1,t):
            if(a[i]>a[j]):
                res+=1
    return res
t1 = tent(A)
t2 = tent(A+A)-2*t1
ans = (t1*k%MOD + t2*(k*(k-1))//2%MOD)%MOD
print(ans)
