z=input().split()
a=int(z[0])
b=int(z[1])
c=int(z[2])
goukei=a+b+c
count = 0
if a == b and b == c:
    print(0)
    exit()
while 1:
  count += 1
  
  goukei = goukei + 2
#   print(str(count)+':'+str(goukei))
  if goukei>=max([a,b,c])*3 and goukei%3 == 0:
    print(count)
    break