n,x=map(int,input().split())
l=list(map(int,input().split()))
haneru=0
cnt=1
for i in l:
  haneru+=i
  if haneru<=x:
    cnt+=1
    
  else:
    break
    
print(cnt)