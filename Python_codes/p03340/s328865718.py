N=int(input())
A=list(map(int,input().split()))

r,S,R=0,0,0

for l in range(N):
  while r<N:
    if S&A[r]==0:
      S|=A[r]
      r+=1
    else:
      break
  R+=r-l
  S&=~A[l]

print(R)
