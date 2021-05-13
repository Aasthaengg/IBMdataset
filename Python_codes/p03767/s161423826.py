n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
ans = 0
for i in a[1:-n:2]:
    ans += i
print(ans)
