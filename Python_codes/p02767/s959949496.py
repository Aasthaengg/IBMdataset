N=int(input())
X=[int(i) for i in input().split()]

X.sort()

if N%2==0:
    ans=10**10
    for i in range(1,100):
        a=0
        for j in range(N):
            a+=(X[j]-i)**2
        ans=min(ans,a)
else:
    ans=10**10
    for i in range(1,100):
        a=0
        for j in range(N):
            a+=(X[j]-i)**2
        ans=min(ans,a)

print(ans)
