N, K = [int(i) for i in input().split()]
l = sorted([int(i) for i in input().split()], reverse=True)
print(sum(l[:K]))
