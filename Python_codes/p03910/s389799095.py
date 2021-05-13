n = int(input())
l, r = 1, n
while l < r:
    m = (l+r)//2
    if (1+m)*m/2 <= n:
        l = m+1
    else:
        r = m
result = [i for i in range(r+1)]
result[(1+r)*r//2 -n] = -1
for i in result[1:]:
    if i < 0:
        continue
    print(i)