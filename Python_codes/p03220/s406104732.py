n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))
num=0
dist=abs(a-(t-h[0]*0.006))
for i in range(1,n):
    if dist>abs(a-(t-h[i]*0.006)):
        num=i
        dist=abs(a-(t-h[i]*0.006))
print(num+1)
