n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

t2 = a[0]
x = a[0]//2
ans = 1
for i in range(1,n):
  t = abs(x - a[i])
  if t < t2:
    t2 = t
    ans = i
print(a[0],a[ans])