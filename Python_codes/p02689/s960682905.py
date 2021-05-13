N, M = (int(x) for x in input().split())
H=list(map(int, input().split()))
check=[True]*N
ans=N
for i in range(M):
  A, B = (int(x) for x in input().split())
  if check[A-1]==True and H[A-1]<H[B-1]:
    check[A-1]=False
    ans-=1
  elif check[B-1]==True and H[A-1]>H[B-1]:
    check[B-1]=False
    ans-=1
  elif H[A-1]==H[B-1]:
    if check[A-1]==True:
      ans-=1
      check[A-1]=False
    if check[B-1]==True:
      ans-=1
      check[B-1]=False
print(ans)