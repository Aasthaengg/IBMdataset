n,k,s = [int(x) for x in input().split()]
if s == 10**9:
    l = [1]*(n-k) + [s]*k
else:
    l = [s+1]*(n-k) + [s]*k
print(*l)