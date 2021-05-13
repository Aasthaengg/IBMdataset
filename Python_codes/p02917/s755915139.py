n = int(input())
b = [int(x) for x in input().split()]

ans = b[0]
for i in range(1, n-1):
    ans += min(b[i-1], b[i])
ans += b[-1]
print(ans)