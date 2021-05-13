n, a, b = [int(i) for i in input().split()]
citys = [int(i) for i in input().split()]

res = 0

for i in range(n-1):
    if (citys[i+1] - citys[i]) * a < b:
        res += (citys[i+1] - citys[i]) * a
    else:
        res += b

print(res)