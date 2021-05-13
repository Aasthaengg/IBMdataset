N = int(input())
a = [0] + list(map(int,input().split()))

inde = 0
absmax = 0
for i in range(1,N+1,1):
    if absmax <= abs(a[i]):
        inde = i
        absmax = abs(a[i])

ans = []
for i in range(1,N+1,1):
    ans.append([inde,i])

if a[inde]>0:
    for i in range(1,N,1):
        ans.append([i,i+1])
else:
    for i in range(N,1,-1):
        ans.append([i,i-1])

print(len(ans))
for i in range(len(ans)):
    print(ans[i][0],ans[i][1])

