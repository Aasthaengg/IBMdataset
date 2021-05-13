from time import time

t = time()
n,m = list(map(int, input().split()))
k = (1/2) * (2**(m-1))
i = 1
testms = 100*(n-m) + 1900*m
ans = 0
while time()-t<1.9:
    ans = ans + (i*testms)*k
    i += 1
    k = k/2

print(round(ans))