from collections import defaultdict
N,W=map(int,input().split())

wvdic=defaultdict(list)
for i in range(N):
  w,v=map(int,input().split())
  wvdic[w].append(v)
#print(wvdic)  

wv_sorted=sorted(wvdic.items())
#print(wv_sorted)

wvslist=[]
for i in range(len(wv_sorted)):
  slist=[0]
  vlist=sorted(wv_sorted[i][1],reverse=True)
  for v in vlist:
    slist.append(slist[-1]+v)
  wvslist.append((wv_sorted[i][0],slist))
if len(wvslist)<4:
  for _ in range(4-len(wvslist)):
    wvslist.append((-1,[0]))
#print(wvslist)

max_answer=0
for w1 in range(len(wvslist[0][1])):
  ww1=wvslist[0][0]*w1
  v1=wvslist[0][1][w1]
  for w2 in range(len(wvslist[1][1])):
    ww2=wvslist[1][0]*w2
    v2=wvslist[1][1][w2]
    for w3 in range(len(wvslist[2][1])):
      ww3=wvslist[2][0]*w3
      v3=wvslist[2][1][w3]
      for w4 in range(len(wvslist[3][1])):        
        ww4=wvslist[3][0]*w4
        v4=wvslist[3][1][w4]
        ww_total=ww1+ww2+ww3+ww4
        #print(ww1,ww2,ww3,ww4,v1,v2,v3,v4)
        if ww_total<=W:
          vtotal=v1+v2+v3+v4
          max_answer=max(max_answer,vtotal)
          
print(max_answer)