import collections
n = int(input())

a = list(map(int,input().split())) 

b = collections.Counter(a)
l = []

for k,v in b.items():
    if v >= 2:
        l.append((k,v))

l = sorted(l,reverse = True)
if not l:
    print(0)
else:
    if l[0][1] >= 4:
        print(l[0][0]**2)
    else:
        print(l[0][0]*l[1][0])