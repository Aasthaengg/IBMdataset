R,G,B,N=map(int,input().split())
count=0
for r in range(0,N//R+1):
  remain_GB=N-R*r
  for g in range(0,remain_GB//G+1):
    remain_B=remain_GB-G*g
    if remain_B%B==0:
      count+=1
print(count)

