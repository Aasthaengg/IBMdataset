N = int(input())
a = list(map(int, input().split()))

if N == 1:
  print("Yes")
  
else:
  flag = True
  for i in range(N-1):
    if a[len(a)-1-i]-a[len(a)-2-i] < -1:
      flag=False
      break
    if a[len(a)-1-i]-a[len(a)-2-i] == -1:
      a[len(a)-2-i]-=1

  print("Yes") if flag else print("No")