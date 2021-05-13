n, m = map(int, input().split())
n -= 1
dat = list(map(int, input().split()))
iseven = True
for i in range(len(dat)):
    if dat[i] %2 == 1:
        iseven = False
if iseven:
    if m == 0:
        print(2**(n+1))
    else:
        print(0)
else:
    if n == 0:
        print(0)
    else:
        print(pow(2, n))