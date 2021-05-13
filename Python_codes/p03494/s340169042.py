N=int(input())
A=list(map(int,input().split()))
MIN=10**9
for i in range(N):
  count=0
  while 1:
    if A[i] % 2 == 0:
      A[i] //= 2
    else:
      break
    count += 1
  MIN = min(MIN,count)
  if MIN==0:
    print(0)
    exit()
print(MIN)