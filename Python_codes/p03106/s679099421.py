A,B,K=map(int,input().split())
count=0
for i in reversed(range(min(A,B))):
  if A%(i+1)==0 and B%(i+1)==0:
    count+=1
  if count==K:
    print(i+1)
    break