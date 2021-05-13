n = int(input())
b = list(map(int, input().split()))
b.insert(0, b[0])
ans = 0
for i in range(n-1):
    ans += min(b[i], b[i+1])
ans += b[-1]
print(ans)