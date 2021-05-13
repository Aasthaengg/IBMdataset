n = int(input())

r0 = int(input())
r1 = int(input())
max = r1-r0
min = min(r0,r1)
for i in range(n-2):
    r = int(input())
    if max < r-min:
        max = r-min
    if min > r:
        min = r
print(max)