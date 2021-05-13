N,K=map(int,input().split())

answer=0
if K==0:
  answer=N**2
else:
  for i in range(K+1,N+1):
    #print(i,(i-K)*((N+1)//i))
    #print(i,max(0,(N+1)%i-K))
    answer+=(i-K)*((N+1)//i)+max(0,(N+1)%i-K)
    
print(answer)