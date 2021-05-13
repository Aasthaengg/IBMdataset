N=int(input())
A=list(map(int,input().split()))
A.sort()
ans=0
for x in range(N-1):
  if A[x]==A[x+1]:
    ans += 1
    break
if ans==0:
  print("YES")
else:
  print("NO")