nk = [int(s) for s in input().split()]
k = nk[1]

p = [int(s) for s in input().split()]

p.sort()
print(sum(p[:k]))