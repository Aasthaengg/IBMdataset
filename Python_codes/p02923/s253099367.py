n = int(input())
h = list(map(int,input().split()))
c = 0
ans = 0
for i in range(n-1):
    if h[i] < h[i+1]:
        c = -1
    c += 1
    ans = max(c,ans)
print(ans)