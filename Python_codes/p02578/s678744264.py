n = int(input())
a = list(map(int,input().split()))
ans = [0]*n
mini = a[0]
for i in range(1,n):
    if a[i] - mini >= 0:
        mini = a[i]
    else:
        ans[i] = mini - a[i]
        mini

print(sum(ans))