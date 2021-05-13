R,G,B,N=map(int,input().split())

answer=0
for r in range(N//R+1):
  for g in range(N//G+1):
    b_ball=N-r*R-g*G
    if b_ball<0:
      break
    elif b_ball%B==0:
      #print(r,g,b_ball%B)
      answer+=1
      
print(answer)