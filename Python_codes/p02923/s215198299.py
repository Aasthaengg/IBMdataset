n = int(input())
h = list(map(int, input().split()))
cnt = 0
mx = 0
for i in range(n-1) :
    if h[i+1] <= h[i] :
        cnt += 1
    else :
        mx = max(mx, cnt)
        cnt = 0
mx = max(mx, cnt)
print(mx)
