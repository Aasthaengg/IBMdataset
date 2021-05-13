n = int(input())
*a, = map(int, input().split())
s = sum(a)
ans = s
tmp = 0
for i in a[:-1]:
    tmp += i
    ans = min(ans, abs(tmp*2 - s))
print(ans)