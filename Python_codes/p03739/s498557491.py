def f(a):
    mode=1
    s=0
    ans=0
    for i in range(n):
        s+=a[i]
        if mode*s<=0: ans+=abs(s)+1;s=mode
        mode*=-1
    return ans


n=int(input())
a=list(map(int,input().split()))
b=[-a[i] for i in range(n)]

mode=1
s=0
print(min(f(a),f(b)))