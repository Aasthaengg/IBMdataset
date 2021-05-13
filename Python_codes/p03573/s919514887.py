l = [i for i in input().split()]

unique = [x for x in set(l) if l.count(x) == 1]
print(unique[0])
