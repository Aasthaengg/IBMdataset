inp=input()
list=inp.split()
r,D,x=list[0], list[1], list[2]
for i in range(10):
  ans=(int(x)*int(r))-int(D)
  x=ans
  print(ans)