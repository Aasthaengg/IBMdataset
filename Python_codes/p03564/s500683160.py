N = int(input())
K = int(input())

res = 1
for _ in range(N):
    tmp = res * 2
    if tmp > res+K:
        res += K
    else:
        res = tmp
print(res)