n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))
ans=100000000000000
ans1=-1
for i in range(n):
    if abs(a-(t-h[i]*0.006))<ans:
        ans=abs(a-(t-h[i]*0.006))
        ans1=i+1
print(ans1)