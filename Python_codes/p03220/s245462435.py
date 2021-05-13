n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))
idx=0
m=1000000000
for i in range(n):
    tmp=t-(h[i]*0.006)
    if abs(a-tmp)<m:
        idx=i
        m=abs(a-tmp)
print(idx+1)