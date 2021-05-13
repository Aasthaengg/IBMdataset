n,m=map(int,input().split())

num=[0]*n
for i in range(m):
  s_,c_=map(int,input().split())
  
  if s_==1 and c_==0 and n>1:
    print(-1)
    exit()
  elif num[s_-1]==0 or num[s_-1]==c_:
    num[s_-1]=c_
  else:
    print(-1)
    exit()
    
if num[0]==0 and len(num)>1:
  print(str(1)+''.join(map(str,num[1:])))
  
else:
  print(''.join(map(str,num)))