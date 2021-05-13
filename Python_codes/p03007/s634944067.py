n = int(input())
a = sorted(list(map(int,input().split())))
if a[n-1] < 0:
    ans = 2*a[n-1]-sum(a)
    print(ans)
    p,q =a[n-1],a[0]
    for i in range(n-1):
        print(p,q)
        p = p-q
        q = a[i+1]
elif a[0] >= 0:
    ans = sum(a)-2*a[0]
    print(ans)
    p,q = a[0],a[1]
    for i in range(n-2):
        print(p,q)
        p = p-q
        q = a[i+2]
    print(q,p)

else:
    num = 0
    ans = 0
    for i in range(n):
        if a[i] < 0:
            ans -=a[i]
        else:
            if a[i-1] < 0 and a[i] >= 0:
                num = i
            ans += a[i]
    print(ans)
    p = a[0]
    for i in range(num,n-1):
        print(p,a[i])
        p -= a[i]
    q = a[n-1]
    print(q,p)
    q -= p
    for i in range(1,num):
        print(q,a[i])
        q -= a[i]