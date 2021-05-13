n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 1
if a[0] == 0:
  print(0)
else:
  for i in range(len(a)):
    ans *= a[i]
    if ans > 10**18:
      print("-1")
      exit()
    elif i == len(a)-1:
      print(ans)