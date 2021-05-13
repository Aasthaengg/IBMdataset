n=int(input())
lis=list(map(int,input().split()))
       
f_ans=100000000000000
for i in range(min(lis),max(lis)+1):
  ans=0
  for l in lis:
    ans+=(i-l)**2
  f_ans=min(ans,f_ans)
    
print(f_ans)
    
    
