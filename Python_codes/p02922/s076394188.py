a,b=map(int,input().split())
ans=1
cnt=0
while(ans<b):
    cnt+=1
    ans=cnt*a-(cnt-1)
  
print(cnt)
