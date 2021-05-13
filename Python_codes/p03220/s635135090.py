n=int(input())
t,a=map(int,input().split())
H=list(map(int,input().split()))
x=1000
for i in range(n):
    if x>abs(a-(t-H[i]*0.006)):
        x=abs(a-(t-H[i]*0.006))
        ans=i+1

print(ans)