MOD = 1000000007
n = int(input())
tli = [ int(it) for it in input().split() ]
ali = [ int(it) for it in input().split() ]
#print (tli,ali)

mav1 = max(tli)
mav2 = max(ali)
mav = mav1
#print (mav1,mav2)
if (mav1!=mav2):
  print (0)
else:
  mai1 = tli.index(mav)
  mai2 = n-1-list(reversed(ali)).index(mav)
  #print (mai1,mai2)
  if (mai2<mai1):
    print (0)
  else:
    s = 1
    tma = -1
    for i in range(0,mai1+1):
      if tli[i]>tma:
        tma = tli[i]
        #print ("lt",tma)
      else:
        s*=(tli[i])
        s%=MOD
        #print ("l")
    tma = -1
    for i in range(n-1,mai2-1,-1):
      if ali[i]>tma:
        tma = ali[i]
        #print ("rt",tma)
      else:
        s*=(ali[i])
        s%=MOD
        #print ("r")
    if (mai2-mai1>1):
      for i in range(mai2-mai1-1):
        s*=mav
        s%=MOD
    print ( s%(1000000007) )
      
    
        
    
 

 