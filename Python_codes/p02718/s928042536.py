N, M = map(int, input().split())
A = list(map(int, input().split()))

s = sum(A)
A = sorted(A, reverse=True)
# Yesのためには、M個の商品全てが、s/(4M)以上の票を獲得することが必要
# つまり、M位の商品がs/(4M)以上の票を獲得していればYes、未満ならNo 
if A[M-1]*(4*M) >= s: print('Yes')
else: print('No')