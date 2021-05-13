n, m = map(int, input().split())
x = [0]*m
for i in range(n):
    a = list(map(int, input().split()))
    for b in a[1:]:
        x[b-1] += 1
print(x.count(n))
