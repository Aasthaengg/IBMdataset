def div_two(x):
    tmp = 0
    cur = x
    while cur % 2 == 0:
        tmp += 1
        cur = cur // 2
    return tmp


n = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(n):
    ans += div_two(A[i])

print(ans)
