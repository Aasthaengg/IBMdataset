import math
N=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(N-1):
    if a[i]==a[i+1]:
        cnt=cnt+1
        a[i]=""
        a[i+1]=""
print(cnt)