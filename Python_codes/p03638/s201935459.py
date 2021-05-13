H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
lis = []
for i in range(N):
  for _ in range(A[i]):
    lis.append(str(i+1))
ans= []
for i in range(H):
  if i%2==0:
    add = lis[:W]
  else:
    add = lis[:W][::-1]
  ans.append(' '.join(add))
  lis = lis[W:]
print(*ans,sep='\n')