N, K = [int(i) for i in input().split()]

stics = [int(i) for i in input().split()]

stics = sorted(stics, reverse=True)

print(sum(stics[:K]))