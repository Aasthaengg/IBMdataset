n = int(input())
a1 = (list(map(int, input().split())))
a2 = (list(map(int, input().split())))
ans = a1[0] + sum(a2)
tmp = ans
for i in range(1, n):
    tmp += a1[i] - a2[i - 1]
    ans = max(ans, tmp)

print(ans)