#import operator
n = int(input())
l = set()
cnt = 1
d = {}
o = {}
for i in range(n):
    s,p = input().split()
    p = int(p)
    d[(s, p)] = cnt
    if s in o:
        x = o[s]
        x.append(p)
        o[s] = x

    else:
        o[s] = [p]

    l.add(s)
    cnt = cnt+1

w = list(l)
w.sort()
k = []
#print("  ")
for i in w:
    m = o[i]
    m.sort(reverse = True)
    for j in m:
        #print(i,j,d[(i,j)])
        k.append(d[(i,j)])

for h in k:
    print(h)