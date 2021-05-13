from collections import Counter
H,W,N = map(int,input().split())
ab = []
corner = []
countlist = [0 for i in range(10)]
for i in range(N):
    a,b = map(int,input().split())
    for h in range(-2,1):
        for w in range(-2,1):
            if 1 <= a+h <= H-2 and 1 <= b+w <= W-2:
                corner.append((a+h,b+w))
cc = Counter(corner)
clist = list(cc.values())
clistc = Counter(clist)
for k,v in clistc.items():
    countlist[k] += v
countlist[0] = (H-2)*(W-2) - sum(countlist)
for i in countlist:
    print(i)