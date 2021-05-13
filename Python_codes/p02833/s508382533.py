N=int(input())
if N%2==1:
  print(0)
else:
  score=0
  while N>=10:
    score+=N//10
    N=N//5
  print(score)