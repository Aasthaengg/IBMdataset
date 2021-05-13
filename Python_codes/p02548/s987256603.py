import math
def II(): return int(input())
N=II()
ans=0
Ceiling=math.floor((N-1)**0.5)
#print(Ceiling)
for i in range(1,Ceiling+1):  
    Sq=i*i
    A=N-Sq
    if A>i:
      ans+=int(2*math.ceil(A/i)-1)
      #print(ans,1)
    else:
      ans+=1
      #print(ans,2)
print(ans)