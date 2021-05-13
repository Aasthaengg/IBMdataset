a,b,c,d,e,f=map(int,input().split())

water_g=[]
for i in range(f//100+1):
  for j in range(f//100+1):
#    print(i,j)
    w=100*a*i + 100*b*j
    if w<=f:
      water_g.append(w)
    else:
      break
water_g=sorted(list(set(water_g)),reverse=True)

sugar_g=[]
for i in range(f*e//100):
  for j in range(f*e//100):
    s=c*i + d*j
    if s<=f:
      sugar_g.append(s)
    else:
      break
sugar_g=sorted(list(set(sugar_g)),reverse=True)

#print(water_g, sugar_g)

ans_water=100*a
ans_sugar=0
for water in water_g:
  if water==0:
    break
  for sugar in sugar_g:
    if water+sugar<=f and sugar/water<=e/100:
      if sugar/(sugar+water)>ans_sugar/(ans_sugar+ans_water):
        ans_water=water
        ans_sugar=sugar
print(ans_water+ans_sugar,ans_sugar)