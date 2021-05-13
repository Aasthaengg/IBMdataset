n,k=[int(x) for x in input().split()]
l=[int(x) for x in input().split()]

l.sort()
l.reverse()
print(sum(l[:k]))