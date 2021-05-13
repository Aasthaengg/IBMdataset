n = int(input())
m=list(map(int,input().split()))
k=0
r=0
for i in range(n):
    if m[i]<k:
        r=1
        break
    k=max(k,m[i]-1)
if r==1:
    print('No')
else:
    print('Yes')
