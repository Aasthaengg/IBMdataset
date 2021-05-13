n = int(input())
k = int(input())

res = float('inf')
for i in range(n+1):
    num = 1
    for c in range(n):
        if c < i:
            num *= 2
        else:
            num += k
    res = min(res, num)

print(res)