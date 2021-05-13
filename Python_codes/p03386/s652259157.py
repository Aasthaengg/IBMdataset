a, b, k = map(int, input().split())

m = set(range(a, min(a+k, b)))
n = set(range(max(a, b-k+1), b+1))
l = m | n

for i in sorted(l):
    print(i)
