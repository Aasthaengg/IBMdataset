h,w,a,b = [int(x) for x in input().split()]
for i in range(h):
  if i<h-b:
    z = "0"*a
    o = "1"*(w-a)
    print(z+o)
  else:
    z = "0"*(w-a)
    o = "1"*a
    print(o+z)