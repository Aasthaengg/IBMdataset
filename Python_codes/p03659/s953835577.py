n = int(input())
a = list(map(int,input().split()))

l = sum(a)
r = 0
ans = 10**20

for i in a[:-1]:
    l -= i
    r += i
    ans = min(ans, abs(l - r))

print(ans)
