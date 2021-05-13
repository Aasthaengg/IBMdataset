#w1<=wi<w1+3
from itertools import product
n,w_max = map(int, input().split( ))
w = {}
w1,v1 = map(int, input().split( ))
w[w1] = [v1]
w2 = w1+1
w3 =w2+1
w4 = w3+1
w[w2] = [0]
w[w3] = [0]
w[w4] = [0]
for i in range(n-1):
    wi,vi=map(int, input().split( ))
    w[wi].append(vi)

for wi in w:
    w[wi].sort(reverse = True)
#print(w)
ans = 0
l1 = len(w[w1])+1
l2 = len(w[w2])+1
l3 = len(w[w3])+1
l4 = len(w[w4])+1
for i1,i2,i3,i4 in product(range(l1),range(l2),range(l3),range(l4)):
    if w1*i1+w2*i2+w3*i3+w4*i4<=w_max:
        ans = max(ans,sum(w[w1][:i1])+sum(w[w2][:i2])+sum(w[w3][:i3])+sum(w[w4][:i4]))###

print(ans)

