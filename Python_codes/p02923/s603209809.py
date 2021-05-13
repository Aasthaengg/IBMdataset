n = int(input())
h = list(map(int,input().split()))
a = h[0]
m = 0
ans = 0
for i in range(1,n):
    if a >= h[i]:
        m += 1
    else:
        ans = max(ans,m)
        m = 0
    a = h[i]
print(max(ans,m))