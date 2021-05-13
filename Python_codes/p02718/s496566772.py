n,m=map(int,input().split())
I=list(map(int,input().split()))
num=0
for i in range(n):
    if I[i]>=(sum(I)/(4*m)):
        num+=1
if num>=m:
    print("Yes")
else:
    print("No")
