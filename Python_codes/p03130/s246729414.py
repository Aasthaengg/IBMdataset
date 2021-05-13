import collections
a=collections.Counter(open(0).read().split())
v,c=zip(*a.most_common())
print("YES" if c[0]==c[1]==2 and c[2]==c[3]==1 else "NO")