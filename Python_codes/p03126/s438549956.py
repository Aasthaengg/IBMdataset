n,m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
  A[i].pop(0)
 
ans = 0
for j in range(1,m+1):
  if all(j in A[i] for i in range(len(A))) == True:
    ans += 1
 
print(ans)