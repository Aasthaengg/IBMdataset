n = int(input())
a = list(map(int, input().split()))
b = sum(a)
c = 0
for i in range(n):
  c += a[i]
  if c >= b / 2:
    k = i
    break
cut1 = c - (b - c)
cut2 = b - c + a[k] - (c - a[k])
ans = min(cut1, cut2)
print(ans)