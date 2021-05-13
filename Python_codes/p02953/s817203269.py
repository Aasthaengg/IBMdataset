import sys
n=int(input())
h=list(map(int,input().split()))

for i in range(n-1):
    if h[i+1]>h[i]:
        h[i+1]-=1
    elif h[i+1]<h[i]:
        print('No')
        sys.exit()

print('Yes')