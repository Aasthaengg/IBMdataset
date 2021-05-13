N,K,S=map(int,input().split())
ans=[S]*K

if N-K>=S:
  ans.extend([S+1]*(N-K))
else:
  ans.extend([1]*(N-K))
  
print(*ans)