import collections
a,b,c =map(int,input().split())
ls = [a,b,c]
counter = collections.Counter(ls)
print(len(counter))
