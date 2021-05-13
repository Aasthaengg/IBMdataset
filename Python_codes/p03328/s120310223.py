a, b = map(int,input().split())
ans = -a
for i in range(b - a): ans += i
print(ans)  