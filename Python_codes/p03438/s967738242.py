import sys
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

asum = sum(a)
bsum = sum(b)

if bsum - asum < 0:
    print("No")
    sys.exit()
    
kai = 0
for i in range(n):
    if b[i] > a[i]:
        kai += (b[i]-a[i]+1) // 2
        
if kai > bsum - asum:
    print("No")
else:
    print("Yes")