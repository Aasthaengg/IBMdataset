n = int(input())
ans = 0
for i in range(1, n+1):
    A1 = i
    c =  n//i
    An = A1 + i * (c - 1)
    ans += (A1 + An) * c // 2

print(ans)