n, k = map(int, input().split())
d = {}
q, r = divmod(n, k)
if r == 0:
    for i in range(k):
        d[i] = q
else:
    for i in range(k):
        if i == 0:
            d[i] = q
        elif 1 <= i <= r:
            d[i] = q+1
        else:
            d[i] = q
#print(d)
ans = 0
if k%2 != 0:
    ans = d[0]**3
else:
    ans = d[0]**3+d[k//2]**3
print(ans)
