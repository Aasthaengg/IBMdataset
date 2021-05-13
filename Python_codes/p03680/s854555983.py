N=int(input())
A=[int(input()) for _ in range(N)]
A.insert(0,0)
i=1
count=0
while True:
  if count>N:
    print(-1)
    break
  lamp=A[i]
  count+=1
  if lamp==2:
    print(count)
    break
  i=lamp