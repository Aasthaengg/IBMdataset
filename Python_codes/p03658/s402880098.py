N, K = [int(i) for i in input().rstrip().split(' ')]
l = sorted(map(int, list(input().rstrip().split(' '))),reverse=True)
print(sum(l[:K]))