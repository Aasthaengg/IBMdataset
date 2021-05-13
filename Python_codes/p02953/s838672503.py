import sys
n = int(input())
h = list(map(int,input().split()))
for i in range(n-1,0,-1):
    if h[i]-h[i-1]>=0:
        pass
    elif h[i]-h[i-1]==-1:
        h[i-1] -= 1
    else:
        break
else:
    print("Yes")
    sys.exit()
print("No")