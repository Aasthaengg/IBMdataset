n, m, x = map(int, input().split())
a = list(map(int, input().split()))
costa = 0
costb = 0
for i in range(x, n):
    if i in a:
        costa += 1
for j in range(x, 0, -1):
    if j in a:
        costb += 1
print(min(costa, costb))