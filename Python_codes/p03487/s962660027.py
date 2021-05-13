n=int(input())
A=list(map(int,input().split()))
D = dict()
for i in range(n):
  if A[i] not in D:
    D[A[i]] = 1
  else:
    D[A[i]] += 1
ans = 0
for i in D:
  if D[i]>=i:
    ans += D[i]-i
  else:
    ans += D[i]
print(ans)