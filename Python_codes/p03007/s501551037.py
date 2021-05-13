n,*a=map(int,open(0).read().split())

plus=[]
minus=[]
for aa in a:
    if aa>=0:
        plus.append(aa)
    else:
        minus.append(aa)

if len(plus)==n:
    plus.sort(reverse=True)
    minus.append(plus.pop())
elif len(minus)==n:
    minus.sort()
    plus.append(minus.pop())

print(sum(plus)-sum(minus))

xy=minus[0]
for i in range(len(plus)-1):
    print('{} {}'.format(xy,plus[i]))
    xy-=plus[i]

print('{} {}'.format(plus[-1],xy))
xy=plus[-1]-xy

for i in range(1,len(minus)):
    print('{} {}'.format(xy,minus[i]))
    xy-=minus[i]

