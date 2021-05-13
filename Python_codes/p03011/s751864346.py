p,q,r = map(int, input().split())
l = [p,q,r]
l.sort()
print(sum(l[:2]))