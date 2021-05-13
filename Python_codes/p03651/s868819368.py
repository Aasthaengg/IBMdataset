import fractions
n, k =map(int, input().split())
dat = list(map(int, input().split()))
x = dat[0]
for i in range(n):
    x = fractions.gcd(x, dat[i])
#print(x)
if k % x == 0 and k <= max(dat):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")