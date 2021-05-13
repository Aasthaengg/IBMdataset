import sys
input = sys.stdin.readline
n=int(input())
count = 0

L=list(range(400,2001,200))
val=len(L)
ans = 0
for i in range(val-1):
    if L[i]<=n<L[i+1]:
        ans=8-count
        break
    else:
        count+=1
print(ans)
