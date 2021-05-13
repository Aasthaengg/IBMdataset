n=int(input())
H=list(map(int,input().split()))

isOK=True
for i in range(n-1,0,-1):
    diff=H[i-1]-H[i]
    if diff<1:
        pass
    elif diff==1:
        H[i-1]-=1
    else:
        isOK=False
        break

if isOK:
    print("Yes")
else:
    print("No")