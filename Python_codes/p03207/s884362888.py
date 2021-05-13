n = int(input())
p = [int(input()) for i in range(n)]
m = 0
ans = 0
for i in range(n):
    m = max(p[i],m)
    ans += p[i]
print(ans - m//2)