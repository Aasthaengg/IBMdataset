D=int(input())
*c,=map(int,input().split())
# for Greedy
ci=[(c[i-1],i) for i in range(1,27)]
ci=[(0,0)]+ci
# ci=[(0,0)]+sorted(ci,reverse=True)

last=[[0]*27]*(D+1)
S=[[0]*27]*(D+1)
DP=[[0]*27]*(D+1)
T=[0]*(D+1)

for d in range(1,D+1):
    *S[d],=map(int,input().split())
    S[d]=[0]+S[d]
    
for d in range(1,D+1):
    T[d] = int(input())

def do_id(i,d):
    dn=0
    last[d][i]=d    
    for k in range(1,27):
      if k!=i:
        dn += ci[k][0]*(d-last[d][k])
    return S[d][i]-dn

Satis=0  
for d in range(1,D+1):
    Satis+=do_id(T[d],d)
    print(Satis)
  
def cal():  
  for d in range(1,D+1):
    mxid=0
    mxi,mxd=0,0
    for i in range(1,27):
      tc,ti=ci[i]
      doid=do_id(ti,d)
      if doid>mxid:
           mxid=doid
           mxi,mxd=ti,d
    DP[mxd][mxi]=mxid             
    last[mxd][mxi]=d
  print(DP)    
    

