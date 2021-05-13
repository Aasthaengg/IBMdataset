n, k = [int(n) for n in input().split(' ')]
p = [int(n) for n in input().split(' ')]
p.sort()
print(sum(p[:k]))
