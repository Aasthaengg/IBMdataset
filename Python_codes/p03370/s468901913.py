n,x = map(int,input().split())
m = []
sum_m = 0
min_m = x
for i in range(n):
    m.append(int(input()))
    sum_m += m[i]
    min_m = min(min_m,m[i])
tmp = x - sum_m
print(n+tmp//min_m)