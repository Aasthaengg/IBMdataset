N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
B=T-A
res=abs(B-H[0]*0.006)
num=1
for i in range(N):
    if abs(B-H[i]*0.006)<res:
        res=abs(B-H[i]*0.006)
        num=i+1
print(num)
