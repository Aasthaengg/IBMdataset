N,K = map(int,input().split())

if N==1:
  ans = K
elif K==1:
  ans = N
else:
  ans =K*(K-1)**(N-1)

print(ans)