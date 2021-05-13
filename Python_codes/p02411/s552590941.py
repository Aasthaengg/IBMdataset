L=[]
c=0
while 1:
  L+=[map(int, raw_input().split())]
  if L[c][0]+L[c][1]+L[c][2]==-3:
    break
  c+=1
  
c=0
while 1:
  if L[c][0]+L[c][1]+L[c][2]==-3:
    break
  if L[c][0]==-1 or L[c][1]==-1 or L[c][0] + L[c][1] < 30:
    print 'F'
  elif L[c][0] + L[c][1] >=80:
    print 'A'
  elif 65 <= L[c][0] + L[c][1] < 80:
    print 'B'
  elif 50 <= L[c][0] + L[c][1] < 65 or 30 <= L[c][0] + L[c][1] < 50 and L[c][2] >= 50:
    print 'C'
  else:
    print 'D'
  c+=1