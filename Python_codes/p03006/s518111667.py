from collections import defaultdict as de
X=de(int)
n=int(input())
a=sorted([list(map(int,input().split()))for i in range(n)])
for i in range(n):
    for j in range(i):
        X[(a[i][0]-a[j][0],a[i][1]-a[j][1])]+=1
print(n-max(X.values(),default=0))