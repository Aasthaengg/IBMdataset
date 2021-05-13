n = int(input())
absum = []
for a in range(1,n//2+1):
    b = n-a
    asum = 0
    bsum = 0
    astr = str(a)
    bstr = str(b)
    for j in range(len(astr)):
        asum = asum + int(astr[j])
    for k in range(len(bstr)):
        bsum = bsum + int(bstr[k])
    absum.append(asum+bsum)
print(min(absum))