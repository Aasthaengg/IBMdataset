max = -(10**9)
n = int(input())
r0 = int(input())
min = r0
for i in range(n-1):
    x = int(input())
    if max < x - min:
        max = x - min
    if x < min:
        min = x
print(max)