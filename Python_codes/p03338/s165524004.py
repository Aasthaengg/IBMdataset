from collections import Counter
N, = list(map(int,input().split()))
S = input()
cx = Counter(S)
cy = Counter()
cm = 0
r = 0
for c in S:
    cx[c] -= 1
    cy[c] += 1
    if cy[c]==1 and cx[c]>=1:
        cm += 1
    elif cy[c]>=2 and cx[c]==0:
        cm -= 1
    r = max(r, cm)
print(r)