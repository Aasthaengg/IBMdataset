n = int(input())
ret = 0
for i in range(n):
    x, v = input().split()
    if v == 'JPY':
        ret += int(x)
    else:
        ret += float(x)*380000

print(ret)