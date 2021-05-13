N = int(input())
count=0
result="No"
for _ in range(N):
  x,y=map(int,input().split())
  if x==y:
    count+=1
    if count==3:
      result="Yes"
  else:
    count=0
print(result)