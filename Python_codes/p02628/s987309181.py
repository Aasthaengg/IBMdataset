N, K = [int(i) for i in input().split(' ')]
p = [int(i) for i in input().split(' ')]
print(sum(sorted(p)[:K]))
