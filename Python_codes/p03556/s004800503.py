n = int(input())
res = 0
for i in range(100000):
    if i * i <= n:
        res = i * i
    else:
        break

print(res)
