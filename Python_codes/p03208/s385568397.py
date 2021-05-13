n,k,*hh = map(int, open(0).read().split())

hh.sort()

ans = hh[k-1]-hh[0]

for i in range(k,n):
    ans = min(ans, hh[i]-hh[i-k+1])

print(ans)