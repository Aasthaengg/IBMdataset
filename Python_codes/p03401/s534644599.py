n = int(input())
a = list(map(int,input().split()))
a.insert(0,0)
a.append(0)
cnt = 0
for i in range(n+1):
  cnt += abs(a[i]-a[i+1])
for i in range(1,n+1):
  ans = cnt
  if a[i-1] <= a[i] <= a[i+1]:
    print(ans)
  elif a[i+1] <= a[i] <= a[i-1]:
    print(ans)
  else:
    if a[i] >= 0:
      ans -=2*min(abs(a[i]-a[i-1]),abs(a[i]-a[i+1]))
      print(ans)
    else:
      ans -=2*min(abs(a[i]-a[i-1]),abs(a[i]-a[i+1]))
      print(ans)