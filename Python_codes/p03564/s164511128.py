n = int(input())
k = int(input())

res = 1
for i in range(n):
    if res * 2 - res < k:
        res *= 2
    else:
        res += k
print(res)