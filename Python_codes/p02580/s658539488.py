
import sys
input=sys.stdin.readline

h,w,m=map(int,input().split())
hs=dict()
ws=dict()
hw=set()
for i in range(m):
    hi,wi=map(int,input().split())
    if hi-1 in ws:
        ws[hi-1]+=1
    else:
        ws[hi-1]=1
    if wi-1 in hs:
        hs[wi-1]+=1
    else:
        hs[wi-1]=1
    hw.add((hi-1,wi-1))    

wmax=max(list(ws.values()))
hh=[]
for ik,wv in ws.items():
    if wv==wmax:
        hh.append(ik)
hmax=max(list(hs.values()))
ww=[]
for jk,hv in hs.items():
    if hv==hmax:
        ww.append(jk)
        
for hi in hh:
    for wi in ww:
        if  not ((hi,wi) in hw):
#            print(hi,wi)
            print(wmax+hmax) 
            sys.exit()
print(wmax+hmax-1)
