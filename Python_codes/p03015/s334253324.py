MOD=10**9+7
L=input()

dp_eq=[2]+[-1]*(len(L)-1)
dp_ne=[1]+[-1]*(len(L)-1)

for i in range(1,len(L)):
  if L[i]=="0":
    dp_eq[i]=dp_eq[i-1]
    dp_ne[i]=3*dp_ne[i-1]%MOD
  elif L[i]=="1":
    dp_eq[i]=2*dp_eq[i-1]%MOD
    dp_ne[i]=(3*dp_ne[i-1]+dp_eq[i-1])%MOD
    
#print(dp)
print((dp_eq[-1]+dp_ne[-1])%MOD)