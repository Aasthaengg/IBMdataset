import numpy as np
import sys
input=sys.stdin.readline # for speed up

n,k=map(int,input().split())
k=min(k,n)
h=list(map(int,input().split()))

c=[0]*n
kn=np.arange(1,k)
h0=h[0]
c0=c[0]
for (ii,hii) in zip(kn,h[1:k]):
  #hii=h[ii]
  cii=c0+abs(hii-h0)
  for (cjj,hjj) in zip(c[1:ii],h[1:ii]):
    if cii>cjj:
      #cii=min(cii,cjj+abs(hii-hjj))
      if hii==hjj:
        #cii=min(cii,cjj)
        cii=cjj
      elif hii>hjj:
        if cii>cjj+hii-hjj:
          cii=cjj+hii-hjj
      elif cii>cjj-hii+hjj:
        cii=cjj-hii+hjj
  c[ii]=cii
"""
c[1]=c[0]+abs(h[1]-h[0])
c[2]=min(c[0]+abs(h[2]-h[0]),c[1]+abs(h[2]-h[1]))
c[3]=min(c[0]+abs(h[3]-h[0]),c[1]+abs(h[3]-h[1]),c[2]+abs(h[3]-h[2]))
"""
#print(c)
kn=np.arange(k,n)
for (ii,hii,hiik) in zip(kn,h[k:n],h[0:n-k]):
  #hii=h[ii]
  cii=c[ii-k]+abs(hii-hiik)
  for (cjj,hjj) in zip(c[ii-k+1:ii],h[ii-k+1:ii]):
    if cii>cjj:
      #cii=min(cii,cjj+abs(hii-hjj))
      if hii==hjj:
        #cii=min(cii,cjj)
        cii=cjj
      elif hii>hjj:
        if cii>cjj+hii-hjj:
          cii=cjj+hii-hjj
      elif cii>cjj-hii+hjj:
        cii=cjj-hii+hjj
  c[ii]=cii
  #print(c)
print(c[n-1])