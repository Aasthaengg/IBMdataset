n = int(input())
a = list(map(int,input().split()))
ma1 = [1]*n
ma2 = [0]*n
mi2 = [0]*n

if n ==0:
    if a[0]==1:
        print(1)
        exit()
    else:
        print(-1)
        exit()

for i in range(1,n):
    ma1[i]=ma1[i-1]*2-a[i]
    if ma1[i]<0:
        print(-1)
        exit()
if n == 1:
    if a[0]==1:
        print(-1)
        exit()
    if a[0]==0:
        if a[1]==1:
            print(2)
            exit()
        elif a[1]==2:
            print(3)
            exit()
        else:
            print(-1)
            exit()

ma2[n-1]=a[n]
ma2[n-2]=ma2[n-1]
mi2[n-1]=a[n]
mi2[n-2]=mi2[n-1]//2 + mi2[n-1]%2
if n!=2:
    for i in range(2,n):
        ma2[n-1-i]=min(ma2[n-i]+a[n-i+1],2**(n-i)-a[n-i])
        mi2[n-1-i]=(mi2[n-i]+a[n-i+1])//2 + (mi2[n-i]+a[n-i+1])%2
        if mi2[n-1-i]>ma2[n-1-i]:
            print(-1)
            exit()
ma2 = [1]+ma2
ans = 0
for i in range(n):
    ans += min(ma1[i],ma2[i])
ans +=sum(a)

print(ans)
