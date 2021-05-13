n=int(input())
a=list(map(int,input().split()))

rem=-1
while True:
    a=sorted(a)
    if a[0]==rem:
        print(a[0])
        break
    rem=a[0]
    for i in range(1,n):
        a[i]%=rem
        if a[i]==0:
            a[i]+=rem