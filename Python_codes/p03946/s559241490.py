N, T = map(int,input().split())
price = list(map(int,input().split()))
benefit = [0] * N
ans = 1
pr_low = float("inf")
be_max = 0
for i in range(N):
    if pr_low > price[i]:
        pr_low = price[i]
    else:
        benefit[i] = price[i] - pr_low
        if be_max < benefit[i]:
            be_max = benefit[i]
            ans = 1
        elif be_max == benefit[i]:
            ans += 1
print(ans)