l=[int(x) for x in input().rstrip().split()]
l.sort()
print(sum(l[:2]))