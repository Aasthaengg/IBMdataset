n = int(input())
a = list(int(x) for x in input().split() if int(x)%2==0)
ok = True
for i in a:
  if i%3!=0 and i%5!=0:
    print('DENIED')
    ok = False
    break
if ok:
  print('APPROVED')