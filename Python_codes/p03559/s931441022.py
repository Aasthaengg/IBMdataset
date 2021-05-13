from bisect import bisect

n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
c = sorted(map(int, input().split()))

ans = 0
bb = [n-bisect(c, b[i])  for i in range(n)]
bbb = []
tmp = 0
for i in range(n)[::-1]:
    tmp += bb[i]
    bbb.append(tmp)
bbb = bbb[::-1]
j = 0
while i < n:
    j = bisect(b, a[i], j,n-1)
    if b[j] <= a[i]:
        break
    ans += bbb[j]
    i += 1

print(ans)
