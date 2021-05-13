n = int(input())
a = sorted(list(map(int,input().split())))
am = a[-1]+1
div = [1]*am
ans = 0

for i in range(n-1):
  a_i = a[i]
  if div[a_i]:
    for j in range(a_i,am,a_i):
      div[j] = 0
    if a_i < a[i+1]:
      ans += 1
if div[-1]:ans += 1
print(ans)

