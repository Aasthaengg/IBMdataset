m,n = map(int, input().split())
if n >= 1<<m:
  print(-1)
   
else:
  if m == 1:
    if n == 1:
      print(-1)
    else:
      print(0,0,1,1)
  else:
    ans = [i for i in range((1<<m)-1, -1, -1)]
    ans.remove(n)
    ans.append(n)
    for i in range(1<<m):
      if i == n:
        continue
      else:
        ans.append(i)
    ans.append(n)
    print(" ".join(map(str, ans)))
