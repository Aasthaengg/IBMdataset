mod=10**9+7
n=int(raw_input())
t=map(int,raw_input().split())
a=map(int,raw_input().split())

if t[n-1]!=a[0]:
    print(0)
    exit()

ans=1
for i in xrange(n):
    if i==0 or i==n-1:
        continue
    elif t[i]>t[i-1]:
        if a[i]<t[i] and a[i]==a[i+1]:
            print(0)
            exit()
        elif a[i]!=t[i] and a[i]!=a[i+1]:
            print(0)
            exit()
    else:
        if t[i]==a[i]:
            if a[i]==a[i+1]:
                ans=(ans*t[i])%mod
        elif t[i]>a[i]:
            if a[i]==a[i+1]:
                ans=(ans*a[i])%mod
        elif a[i]>t[i]:
            if a[i]==a[i+1]:
                ans=(ans*t[i])%mod
            else:
                print(0)
                exit()
print(ans%mod)
