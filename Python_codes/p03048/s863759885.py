R,G,B,N =map(int,input().split())

cnt =0
    
for r in range(int(N/R)+1):
  ball = N-r*R 
  for g in range(int(ball/G)+1):
    res = N- (r*R+g*G)
    if  res >=0 and res%B ==0:
      cnt+=1
    
print(cnt)
            
