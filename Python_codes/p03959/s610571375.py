import sys
input = sys.stdin.readline
n=int(input())
t=list(map(int,input().split()))
a=list(map(int,input().split()))
t=[0]+t+[t[-1]]
a=[a[0]]+a+[0]
ans=1
#print(t,a)
for i in range(n):
    if t[i]<t[i+1]:
        if a[i+1]<t[i+1]:
            ans=0
            break
    if a[i]>a[i+1]:
        if t[i]<a[i]:
            ans=0
            break
    if t[-2]!=a[1]:
        ans=0
        break
    if t[i]==t[i+1] and a[i+1]==a[i+2]:
        ans=(ans*(min(t[i+1],a[i+1])))%(10**9+7)
print(ans)