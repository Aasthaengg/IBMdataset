# coding: utf-8
yama=[0 for i in range(int(input()))]
t=list(map(int,input().split()))
a=list(map(int,input().split()))

check=0
for i in range(len(yama)):
    if check!=t[i]:
        check=t[i]
        yama[i]=check
    else:
        yama[i]=-check
check=0
for i in range(len(yama)):
    if yama[len(yama)-i-1]>0 and yama[len(yama)-i-1]>a[len(yama)-i-1]:
        print(0)
        exit()
    if check!=a[len(yama)-i-1]:
        check=a[len(yama)-i-1]
        if yama[len(yama)-i-1]>0 and yama[len(yama)-i-1]>check:
            print(0)
            exit()
        yama[len(yama)-i-1]=check
    else:
        if yama[len(yama)-i-1]<0:
            yama[len(yama)-i-1]=max(-check,yama[len(yama)-i-1])

x=1
for i in yama:
    if i<0:
        x=(x*-i)%1000000007

print(x)
