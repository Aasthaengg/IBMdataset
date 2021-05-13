N,K = map(int,input().split())
A = list(map(int,input().split()))
mod = 1000000007
ans = 0
list = [[0,0] for i in range(N)]
I = 0
J = 0
for i in range(N):
  for j in range(i):
    if A[j] < A[i]:
      list[i][0] += 1
      I += 1
      J += 1
  for k in range(i+1,N):
    if A[k] < A[i]:
      list[i][1] += 1
      J += 1
#print(list)
for i in range(N):
  ans += K*list[i][1] + K*(K-1)*(list[i][0]+list[i][1])//2                     
print(ans%mod)
                          
                          
                          
                          
                          
                          
                          
         
