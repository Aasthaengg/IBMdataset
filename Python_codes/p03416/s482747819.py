A,B=map(int,input().split())
ans=0
for i in range(A,B+1):
  check1=str(i)
  check2=check1[::-1]
  if check1==check2:
    ans+=1
print(ans)
