n, k = map(int, input().split())
l = sorted([int(i) for i in input().split()], reverse=True)
print(sum(l[:k]))