n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
cnt = n-2
ans = a[0]
for i in a[1:]:
  if cnt==0: break
  elif cnt>=2:
    cnt -= 2
    ans += (i*2)
  else:
    cnt -=1
    ans += i
print(ans)