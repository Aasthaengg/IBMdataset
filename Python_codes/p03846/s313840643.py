n=int(input())
a=list(map(int,input().split()))

icnt=[0]*n
for i in range(n):
    icnt[a[i]]+=1

yn=""
if n%2==0:
    for i in range(n):
        if i%2==0:
            if icnt[i]!=0:
                yn="NO"
                break
        else:
            if icnt[i]!=2:
                yn="NO"
                break
else:
    for i in range(n):
        if i==0:
            if icnt[i]!=1:
                yn="NO"
                break
        elif i%2==0:
            if icnt[i]!=2:
                yn="NO"
                break
        else:
            if icnt[i]!=0:
                yn="NO"
                break
if yn=="NO":
    print(0)
else:
    n2=n//2
    p=10**9+7
    print(pow(2,n2,p))