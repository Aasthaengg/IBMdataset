N, K = list(map(int, input().rstrip().split()))
l = sorted(list(map(int, input().rstrip().split())))
r = sum(l[0:K])
print(r)

