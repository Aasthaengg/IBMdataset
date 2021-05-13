from collections import Counter
A = input()
ctr = Counter(A)

ans = 0
for k,v in ctr.items():
    for k2,v2 in ctr.items():
        if k==k2: continue
        ans += v*v2
print(ans//2 + 1)