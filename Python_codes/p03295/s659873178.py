import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
n,m=map(int,input().split())
a=sorted([tuple(map(int,input().split())) for _ in range(m)])
i=0
cnt=0
k=n
while i<m:
    k=a[i][1]
    if a[i][0]<k:
        while i<m and a[i][0]<k:
            k=min(k,a[i][1])
            i+=1
    if i<m and a[i][0]>=k:
        cnt+=1
    else:
        cnt+=1
        i+=1
print(cnt)