n,k = map(int,input().split())
lis = list(map(int,input().split()))
ans = 0
for i in range(n):
    for j in range(n-i+1):
        num = lis[:i]
        if j > 0:
            num += lis[-j:]
        if len(num) <= k:
            cnt = min(len(num),k-len(num))
            num.sort()
            for h in range(cnt):
                num[h] = max(0,num[h])
            ans = max(ans,sum(num))
print(ans)