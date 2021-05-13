n = int(input())
a = list(map(int,input().split()))
a.sort(reverse = True)
b = True
wh = 0
for i in range(n - 1):
  if b == False:
    b = True
    continue
  if a[i] == a[i + 1]:
    b = False
    if wh == 0:
      wh = a[i]
    else:
      print(wh * a[i])
      exit()
print(0)