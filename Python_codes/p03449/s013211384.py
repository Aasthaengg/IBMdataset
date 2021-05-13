n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a1sum, a2sum, ans = 0, 0, 0
a2sumall = sum(a2)
for i in range(n):
    a1sum += a1[i]
    a2sum += a2[i]
    ans = max(ans, a1sum + a2sumall - a2sum + a2[i])
print(ans)
