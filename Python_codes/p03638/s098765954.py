H,W = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))
ans = []
for i in range(N):
  for _ in range(A[i]):
    ans.append(i+1)
cnt = 0
for i in range(0,H*W,W):
  if cnt % 2 != 0:
    print(*ans[i:i+W][::-1],end="\n")
  else:
    print(*ans[i:i+W],end="\n")
  cnt += 1