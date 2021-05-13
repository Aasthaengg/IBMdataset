n,k,q, *aa = map(int, open(0).read().split())

scores = [k-q]*n

for a in aa:
    scores[a-1] += 1

for s in scores:
    if s<=0:
        print('No')
    else:
        print('Yes')