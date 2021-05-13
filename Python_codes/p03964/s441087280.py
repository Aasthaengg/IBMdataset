n=int(input())
ta=[list(map(int,input().split())) for i in range(n)]
T=ta[0][0]
A=ta[0][1]
for i in range(1,n):
    t,a=ta[i]
    if T%t==0:
        s=T//t
    else:
        s=T//t+1
    if A%a==0:
        b=A//a
    else:
        b=A//a+1
    T=t*max(s,b)
    A=a*max(s,b)
print(T+A)