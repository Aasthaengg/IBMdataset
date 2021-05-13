N=int(input())
*A,=map(int,input().split())
*B,=map(int,input().split())

if sum(A)<sum(B):
  print(-1)
  exit()
  
#A,B = map(sorted,(A,B))

res=0
count=0
for i in range(N):
  if B[i]>A[i]:
    res += B[i]-A[i]
    count += 1
    
if count==0:
  print(0)
  exit()
  
plus = [A[i]-B[i] for i in range(N) if A[i]>B[i]]
plus = sorted(plus,reverse=True)

for i in range(len(plus)):
  res -= plus[i]
  count += 1
  if res<=0:break
    
print(count)