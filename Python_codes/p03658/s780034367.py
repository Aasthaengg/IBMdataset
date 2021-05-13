n,k = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
l.sort(reverse = True)
la = l[:k]
print(sum(la))