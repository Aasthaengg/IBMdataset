d={1:0,2:0,3:0,4:0}
for i in range(3):
  a,b=map(int,input().split())
  d[a]+=1;d[b]+=1
print("YNEOS"[d[1]==3or d[2]==3or d[3]==3or d[4]==3::2])