n, x = map(int, input().split())
l = list(map(int, input().split()))
d = [0]*(n+1)
counter = 1
for i in range(1,n + 1):
    d[i] = d[i - 1] + l[i - 1]
    if d[i] <= x:
        counter += 1
print(counter)
