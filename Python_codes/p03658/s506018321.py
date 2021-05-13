N, K = map(int, input().split())
l = list(map(int, input().split()))
x = sorted(l)[::-1]
print(sum(x[:K]))