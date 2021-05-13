[a,b,c] = [int(i) for i in input().split(" ")]
goukei = 0
for i in range(1,a+1):
  kurainowa = 0
  kisuu = [int(k) for k in list(str(i))]
  
  for j in range(0,len(kisuu)-1+1):
    kurainowa = kurainowa + kisuu[j]
  if kurainowa < c+1 and b-1 <kurainowa :
    goukei = goukei + i
print(goukei)