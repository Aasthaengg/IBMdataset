n = int(input())
a = list(input())
b = list(input())
c = list(input())
ans = 0
for i in range(n):
  if len(set([a[i],b[i],c[i]])) == 1:
    continue
  elif len(set([a[i],b[i],c[i]])) == 2:
    ans += 1
  else:
    ans += 2
print(ans)