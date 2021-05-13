import sys
input = sys.stdin.readline

n=int(input())
L=list(map(int,input().split()))
MIN = 1<<30
ans = 0
for i in L:
    MIN = min(MIN,i)
    if i<=MIN:
        ans+=1
print(ans)

