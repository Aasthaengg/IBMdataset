mod = 1000000007
n,m = [int(x) for x in input().split()]
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

xtot=0
ytot=0
mult=n-1
multdiff=mult-2
for i in range(1,n):
    xadd = x[i]-x[i-1]
    xadd = (xadd%mod * abs(mult)%mod)%mod
    xtot = (xtot%mod + xadd%mod)%mod

    mult+=multdiff
    multdiff-=2

mult=m-1
multdiff=mult-2
for i in range(1,m):
    yadd = y[i]-y[i-1]
    yadd = (yadd%mod * abs(mult)%mod)%mod
    ytot = (ytot%mod + yadd%mod)%mod

    mult+=multdiff
    multdiff-=2

print((xtot%mod*ytot%mod)%mod)
