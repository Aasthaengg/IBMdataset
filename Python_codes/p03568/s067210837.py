N=int(input())
A=list(map(int,input().split()))
all=1
bad=1
for i in range(N):
  all*=3
  if A[i]%2==0:
    bad*=2
print(all-bad)
