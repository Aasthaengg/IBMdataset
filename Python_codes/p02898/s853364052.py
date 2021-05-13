n, k = [int(i) for i in input().split()]
hs = [int(i) for i in input().split()]
print (sum([1 if i >= k else 0 for i in hs]))