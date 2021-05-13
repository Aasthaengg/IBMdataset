A,B,C=map(int,input().split())

count=0
while True:
  if A==B and B==C:
    if A%2 == 0:
      count=-1
    break
  elif A%2==1 or B%2==1 or C%2==1:
    break
  else:
    A,B,C=(B+C)//2,(A+C)//2,(A+B)//2
    count+=1
  pass
print(count)