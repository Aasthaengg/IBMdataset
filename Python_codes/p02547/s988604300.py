n=int(input())
cnt=0
ans='No'
for i in range(n):
  d1,d2=map(int,input().split())
  if d1==d2:
    cnt+=1
  else:
    cnt=0
  if cnt==3:
    ans='Yes'
    break
print(ans)  