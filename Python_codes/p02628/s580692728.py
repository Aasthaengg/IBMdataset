N, K = list(map(int, input().split()))
p = list(map(int, input().split()))
print(sum(list(sorted(p))[0:K]))
