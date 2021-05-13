n = int(input())
a = list(map(int, input().split()))
c = [False]*8
k = 0
ans = 0
for i in range(n):
  cn = a[i]//400
  if cn < 8:
    if c[cn] == False:
      ans += 1
      c[cn] = True
  else:
    k += 1
print(max(1, ans), ans + k)
