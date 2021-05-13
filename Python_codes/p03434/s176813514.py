input()
l = list(map(int,input().split()))
list.sort(l,reverse=True)
ans = 0
for i in range(len(l)):
  if i % 2 == 0:
    ans += l[i]
  else:
    ans -= l[i]
print(ans)