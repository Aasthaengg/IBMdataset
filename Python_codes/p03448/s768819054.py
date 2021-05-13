A = int(input())
B = int(input())
C = int(input())
X = int(input())
c=0
for i in range(0,A+1):
  Y=X-i*500
  for j in range(0,B+1):
    Y=Y-j*100
    for l in range(0,C+1):
      Y=Y-l*50
      if Y == 0:
        c += 1
        Y=Y+l*50
      else :
        Y = Y + l*50
    else :
      Y = Y+j*100
print(c)
  

