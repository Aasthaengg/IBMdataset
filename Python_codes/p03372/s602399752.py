from bisect import bisect_right,bisect_left
N,C=map(int,input().split())
S=[[int(i) for i in input().split()] for i in range(N)]
Way1=[S[0][1]-S[0][0]]
p1=[]
if Way1[0]>0:
  p1.append(0)
for i in range(1,N):
  Way1.append(Way1[i-1]+S[i][1]-(S[i][0]-S[i-1][0]))
  if p1==[] and Way1[i]>0:
    p1.append(i)
  elif p1!=[]:
    if Way1[p1[-1]]<Way1[i]:
      p1.append(i)
    
Way2=[S[-1][1]-(C-S[-1][0])]
p2=[]
if Way2[0]>0:
  p2.append(N-1)
for i in range(1,N):
  Way2.append(Way2[i-1]+S[N-i-1][1]+(S[N-i-1][0]-S[N-i][0]))
  if p2==[] and Way2[i]>0:
    p2.append(N-i-1)
  elif p2!=[]:
    if Way2[N-1-p2[-1]]<Way2[i]:
      p2.append(N-i-1)
Way2.reverse()
p2.reverse()

ans=0
for i in p1:
  if i!=N-1:
    if bisect_right(p2,i+0.1)<len(p2):
      j=p2[bisect_right(p2,i+0.1)]
      ans=max(ans,Way1[i],Way1[i]-S[i][0]+Way2[j])
    else:
      ans=max(ans,Way1[i])
  else:
    ans=max(ans,Way1[i])
for j in p2:
  if j!=0:
    if bisect_left(p1,j-0.1)>0:
      i=p1[bisect_left(p1,j-0.1)-1]
      ans=max(ans,Way2[j],Way1[i]-(C-S[j][0])+Way2[j])
    else:
      ans=max(ans,Way2[j])
  else:
    ans=max(ans,Way2[j])
    
print(ans)
