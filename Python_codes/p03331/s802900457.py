n = int(input())
res = float('inf')
for a in range(1, int(n/2)+1):
    b = n-a
    tmp = 0
    for c in str(a):
        tmp += int(c)
    for c in str(b):
        tmp += int(c)
    res = min(res, tmp)
print(res)