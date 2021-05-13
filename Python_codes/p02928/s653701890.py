mod = 10**9 + 7
n,k = map(int,input().split())
A = list(map(int,input().split()))

t = 0
for i in range(n):
  for j in range(i+1,n):
    if A[i]>A[j]:
      t += 1

sA = sorted(A)
C = [0]*n
for i in range(1,n):
  if sA[i-1] == sA[i]:
    C[i] = C[i-1]
  else:
    C[i] = i

ans = (t*k) % mod
multi = k*(k-1)//2

for i in range(n):
  ans = (ans + (C[i]*multi) ) %mod
  
print(ans)  