N,K = map(int, input().split())
length = list(map(int, input().split()))

a = sorted(length, reverse=True)
b = a[0:K]
print(sum(b))