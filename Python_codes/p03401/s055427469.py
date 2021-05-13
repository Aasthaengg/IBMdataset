a=int(input())
b=list(map(int,input().split()))
b=[0]+b+[0]
s=0
for i in range(1,a+2):
    s=s+abs(b[i]-b[i-1])
for j in range(1,a+1):
    print(s+abs(b[j+1]-b[j-1])-abs(b[j]-b[j-1])-abs(b[j+1]-b[j]))