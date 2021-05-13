n,k,*hh = map(int, open(0).read().split())

hh.sort(reverse=True)

print(sum(hh[k:]))