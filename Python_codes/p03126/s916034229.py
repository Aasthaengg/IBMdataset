n, m = map(int, input().split())
d = [0] * m

for i in range(n):
    k, *a = list(map(int, input().split()))
    for num in a:
        d[num-1] += 1

c = 0
for num in d:
    if num == n:
        c += 1
print(c)