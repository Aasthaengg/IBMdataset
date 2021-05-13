n = int(input())
l = list(map(int,input().split()))
l.sort()
ans = 0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      a = l[i]
      b = l[j]
      c = l[k]
      if a == b or b == c or c == a:
        continue
      if l[i] + l[j] > l[k]:
        ans += 1
print(ans)
