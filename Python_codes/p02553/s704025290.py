a,b,c,d = map(int,input().split())
max = 10 ** 20 * -1
if a*c >= max:
  max = a*c
if a*d >= max:
  max = a*d
if b*c >= max:
  max = b*c
if b*d >= max:
  max = b*d
  
print(max)
