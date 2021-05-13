input()
# map returns an iterator rather than a list, 
# and an iterator can traverses the data only once.
# so we need to 'list' here
ns=list(map(int,input().split())) 
print(min(ns),max(ns),sum(ns))