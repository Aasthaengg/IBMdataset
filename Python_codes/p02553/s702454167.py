x = list(map(int, input().split()))
a = x[0]
b = x[1]
c = x[2]
d = x[3]

ac = a*c
ad = a*d
bc = b*c
bd = b*d

max = ac
if max<ad:
  max = ad
if max<bc:
  max = bc
if max<bd:
  max = bd
      
print(max)
    

