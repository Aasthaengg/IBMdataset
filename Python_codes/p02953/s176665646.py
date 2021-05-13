n=int(input())
h=list(map(int,input().split()))
if n==1:
    print("Yes")
    exit()
for i in range(1,n):
    if h[i]-h[i-1]<=-1:
        print("No")
        exit()
    elif h[i]-h[i-1]==0:
        pass
    elif h[i]-h[i-1]>=1:
        h[i]-=1
print("Yes")
