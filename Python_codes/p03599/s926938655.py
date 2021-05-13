a,b,c,d,e,f=map(int,input().split())
ans=0
tmp=[str(100*a),'0']
for i in range(1,2**4):
  l=[0]*4
  water=0
  sugar=0
  for j in range(4):
    if i>>j&1:
      l[j]=1
  if l[0]==1:
    water+=100*a
  if l[1]==1:
    water+=100*b
  if water==0:
    pass
  else:
    rest=f-water
    if rest<=0 or (l[2]==l[3]==0):
      pass
    else:
      max_sugar=e*(water//100)
      if l[2]==1 and l[3]==0:
        sugar+=c*(min(rest,max_sugar)//c)
      elif l[3]==1 and l[2]==0:
        sugar+=d*(min(rest,max_sugar)//d)
      elif l[2]==l[3]==1:
        d_max=min(rest,max_sugar)//d
        t=d*d_max
        for i in range(d_max,-1,-1):
          REST=rest-i*d
          Max_sugar=max_sugar-i*d
          t_max=i*d+c*(min(REST,Max_sugar)//c)
          t=max(t,t_max)
        sugar+=t
      tot=sugar+water
      if sugar/tot>ans:
        ans=sugar/tot
        tmp=[str(tot),str(sugar)]
print(' '.join(tmp))