n, a, b = map(int, input().split(' '))
if a+b <= n:
    min_p = 0
else:
    min_p = abs(n-a-b)
max_p = min([a,b])
print(max_p, min_p)