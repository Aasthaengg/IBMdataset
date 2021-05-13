k,t,*aa = map(int, open(0).read().split())
aa.sort(reverse=True)

eligible = min(aa[0], sum(aa[1:]) + 1) + sum(aa[1:])

print(k-min(k,eligible))