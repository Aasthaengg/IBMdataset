import itertools
l = list(map(int,input().split()))

com = list(itertools.combinations(l,2))

k = []
for i in range(len(com)):
    k.append(sum(com[i]))
    
print(min(k))