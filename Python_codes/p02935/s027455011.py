n = int(input())
v = sorted(list(map(int, input().split())))
v[1] += v[0]
ans = 0
for i in range(1, n):
    ans += v[i]/(2**(n-i))
print(ans)