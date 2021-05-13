from fractions import gcd
N = int(input())
A = list(map(int, input().split()))
A.sort()
T = [A[0]]
for i in range(1,len(A)):
  if A[i]//A[0] != 0:
    T.append(A[i])
  else:
    pass

ans = A[0]
for i in range(len(T)):
  ans = gcd(ans,T[i])
print(ans)