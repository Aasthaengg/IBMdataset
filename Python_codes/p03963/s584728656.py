LL = input().split()
N = int(LL[0])
K = int(LL[1])
if N ==1 or K ==1:
  ans = N*K
else:
  ans =K*(K-1)**(N-1)
print(ans)
