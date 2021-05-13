nn, kk = list(map(int,input().split()))
hh = list(map(int,input().split()))
hh.sort()
if nn <= kk:
    print(0)
else:
    print(sum(hh[0:nn-kk]))