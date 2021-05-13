n, k = [int(i) for i in input().split()]
p = sorted([int(i) for i in input().split()])
print(sum(p[:k]))