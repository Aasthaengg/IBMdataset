lim, pol = map(int,input().split())

count = 0
num = 0
if pol == 0:
    count = lim * lim
else:
    for kk in range(pol, lim + 1):
        num = (lim - lim % kk) / kk
        count += (kk - pol) * num
        if lim % kk >= pol:
            count += lim % kk - pol + 1

print(int(count))