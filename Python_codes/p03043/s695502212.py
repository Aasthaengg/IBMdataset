n,k = map(int,input().split())
asum = 0
for i in range(1,n+1):
    a = i
    if a < k:
        for j in range(1,21):
            if a < k:
                a *= 2
            if a >= k:
                break
        asum += (1/n)*((1/2)**j)
    else:
        asum += (1/n)
print(asum)