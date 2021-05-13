n,a,b = map(int,input().split())

kumi = n // (a + b)

kumi_ao = kumi * a

nokori = n % (a+b)

if nokori <= a:
  nokori_ao = nokori
  
else:
  nokori_ao = a
  
print(kumi_ao+nokori_ao)