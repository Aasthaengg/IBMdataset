N=int(input())
H=list(map(int, input().split()))
L=[float('inf')]*N
L[N-1]=H[N-1]
for i in range(1,N):
  a=H[N-i-1]
  if a-1>L[N-i]:
    print('No')
    exit()
  L[N-i-1]=min(a,L[N-i])
else:
  print('Yes')