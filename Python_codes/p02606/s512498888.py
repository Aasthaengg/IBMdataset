L, R, d = map(int, input().split())
t = 1
res = 0
while t * d <= R: 
    if L <= t * d <= R:
        res += 1
    t += 1
print(res)
