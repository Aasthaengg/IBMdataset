n = int(input())
l = [0]*n
r = [0]*n
ans = 0
for i in range(n):
    l[i], r[i] = map(int, input().split())
    ans += r[i] - l[i] + 1
print(ans)