from collections import deque
x,y,z,k = map(int,input().split())
a = sorted(list(map(int,input().split())),reverse=True)
b = sorted(list(map(int,input().split())),reverse=True)
c = sorted(list(map(int,input().split())),reverse=True)
ans = []
for i in range(x):
    for j in range(y):
        for m in range(z):
            if (i+1)*(j+1)*(m+1) <= k:
                ans.append(a[i]+b[j]+c[m])
            else:
                break

ans.sort(reverse=True)
for i in range(k):
    print(ans[i])
