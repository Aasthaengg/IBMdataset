n = int(input())
absum = []
for a in range(1,n//2+1):
    b = n-a
    asum = 0
    bsum = 0
    alen = len(str(a))
    blen = len(str(b))
    for j in range(alen):
        a0 = (a//(10**j)) % 10
        asum = asum + a0
    for k in range(blen):
        b0 = (b//(10**k)) % 10
        bsum = bsum + b0
    absum.append(asum+bsum)
print(min(absum))  