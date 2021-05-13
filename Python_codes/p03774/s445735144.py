n,m=map(int,input().split())
st=[]
ch=[]
def mht(ax,ay,bx,by):
  return abs(ax-bx)+abs(ay-by)

for i in range(n):
  st.append(list(map(int,input().split())))
for i in range(m):
  ch.append(list(map(int,input().split())))
  
for i in st:
  ax=i[0]
  ay=i[1]
  mn=1000000000
  for (j,k) in zip(ch,range(len(ch))):
    bx=j[0]
    by=j[1]
    mh=mht(ax,ay,bx,by)
    if mh<mn:
      mn=mh
      nm=k
  print(nm+1)
