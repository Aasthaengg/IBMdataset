n, d = map(int, input().split())
d2 = d**2
count=0
for _ in range(n):
    x, y = map(int, input().split())
    if (x**2 + y**2) <= d2:
        count+=1
print(count)