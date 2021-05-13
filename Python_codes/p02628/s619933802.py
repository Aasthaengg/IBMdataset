n, k = map(int, input().split())
l = sorted([int(x) for x in input().split()])

print(sum(l[:k]))