a,b=map(int,input().split())
pfa={}
m=a
for i in range(2,int(m**0.5)+1):
    while m%i==0:
        pfa[i]=pfa.get(i,0)+1
        m//=i
if m>1:pfa[m]=1
pfb={}
m=b
for i in range(2,int(m**0.5)+1):
    while m%i==0:
        pfb[i]=pfb.get(i,0)+1
        m//=i
if m>1:pfb[m]=1
aa=set()
bb=set()
for i in pfa.keys():
    aa.add(i)
for i in pfb.keys():
    bb.add(i)
print(len(aa&bb)+1)