K=int(input())
A=list(map(int,input().split()))
mb=Mb=2
t=1
for i in A[::-1]:
    if Mb//i*i>=mb:
        Ma=(Mb//i+1)*i-1
    else:
        t=0
        break
    if mb%i==0:
        ma=mb
    elif (mb//i+1)*i<=Mb:
        ma=(mb//i+1)*i
    else:
        t=0
        break
    mb=ma
    Mb=Ma
if t:
    print(ma,Ma)
else:
    print(-1)