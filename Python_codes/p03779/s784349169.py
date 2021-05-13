x=int(input())
for i in range(1,10**5):
  now=(i*(i+1))//2
  if now==x:
    print(i)
    break

  if x<now:
    print(i)
    break
