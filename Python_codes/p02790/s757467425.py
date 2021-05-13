a,b = input().split()
aa = a*int(b)
bb = b*int(a)
print(aa if aa<bb else bb)