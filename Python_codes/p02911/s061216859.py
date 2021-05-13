N,K,Q=map(int,input().split())
check=[K-Q]*N
for i in range(Q):
  A=int(input())-1
  check[A]+=1
for i in range(N):
  print("Yes" if check[i]>0 else "No")
