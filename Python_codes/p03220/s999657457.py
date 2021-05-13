n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))
ans=1
cnt=abs(a-(t-h[0]*0.006))
for i in range(1,n):
    if abs(a-(t-h[i]*0.006))<=cnt:
        cnt=abs(a-(t-h[i]*0.006))
        ans=i+1
    else:
        pass
print(ans)