A,B,K = map(int,input().split())
flg = True
for k in range(K):
  if flg:
    if A%2 != 0:
      A-=1
    A//=2
    B+=A
    flg = False
  else:
    if B%2 != 0:
      B-=1
    B//=2
    A+=B
    flg = True

print(A,B)