N,K = [int(x) for x in input().split()]
ans =0
for i in range(K+1,N+1):
  #print((N//i)*(i-K),N%i+1-K)
  ans += (N//i)*(i-K)
  if N%i!=0 and K!=0:
    ans +=max((N%i+1-K),0)
  elif N%i!=0 and K==0:
    ans +=(N%i)
print(ans)