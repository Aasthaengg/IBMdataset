icase=0
if icase==0:
    n=int(input())
    t=[0]*n
    a=[0]*n

    for i in range(n):
        t[i],a[i]=map(int,input().split())
elif icase==1:
    n=5
    t=[3,48,31,231,3]
    a=[10,17,199,23,2]
    ans=6930

ti=t[0]
ai=a[0]
dt=1
for i in range(n-1):
    if ti/t[i+1]>ai/a[i+1]:
        ii=max((ti-dt)//t[i+1]+1,1)
        ti=ii*t[i+1]
        ai=ii*a[i+1]
    else:
        ii=max((ai-dt)//a[i+1]+1,1)
        ti=ii*t[i+1]
        ai=ii*a[i+1]

print(ai+ti)
         
