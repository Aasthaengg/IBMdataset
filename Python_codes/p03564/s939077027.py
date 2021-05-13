N = int(input())
K = int(input())
ans = 1000000000000
for i in range(2 ** N):
    num = 1
    for j in range(N):
        if i & (1 << j):
            num *= 2
        else:
            num += K
    ans = min(ans, num)
print(ans)
