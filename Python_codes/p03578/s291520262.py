N=int(input())
D=list(map(int,input().split()))
M=int(input())
T=list(map(int,input().split()))
D=sorted(D)
T=sorted(T)
i,j=0,0
count=0
while True:
  now=T[i]
  tmp=0
  for k in range(j,N):
    if D[k]==now:
      j=k+1
      count+=1
      i+=1
      break
  else:
    tmp=k
  if count==M:
    print("YES")
    exit()
  if tmp==N-1:
    print("NO")
    exit()
