H,W=map(int,input().split())
N=int(input())
A=list(map(int,input().split()))
ans = []
for i in range(N):
  ans+=[i+1]*A[i]
for i in range(H):
  dum=ans[i*W:(i+1)*W]
  if i%2==0:
    print(*dum[:])
  else:
    print(*dum[::-1])
