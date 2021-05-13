n = int(input())
h = list(map(int,input().split()))
cnt = 0; res = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        cnt += 1
    else:
        cnt = 0
    res = max(res,cnt)
print(res)