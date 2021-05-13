A, B = map(int, input().split())

print(100, 100)

a = A-1
b = B-1

a,b = b,a

qa = a//50
qb = b//50
ra = a%50
rb = b%50
for i in range(50):
  if i%2 == 1:
    print("."*100)
  else:
    if qa == 0:
      if ra == 0:
        print("."*100)
      else:
        print("#."*ra+".."*(50-ra))
        ra = 0
    else:
      print("#."*50)
      qa -= 1
for i in range(50):
  if i%2 == 0:
    print("#"*100)
  else:
    if qb == 0:
      if rb == 0:
        print("#"*100)
      else:
        print(".#"*rb+"##"*(50-rb))
        rb = 0
    else:
      print(".#"*50)
      qb -= 1