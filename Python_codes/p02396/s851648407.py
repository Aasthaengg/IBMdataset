a=[]
while True:
    x = int(input())
    if x == 0:
        break
    a.append(x)

j=1
for i in a:
  print("Case %d: %d" % (j,i))
  j=j+1
