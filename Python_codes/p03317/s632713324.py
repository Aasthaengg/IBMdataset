N,K = (int(X) for X in input().split())
A  = [int(X) for X in input().split()]
Left  = A.index(1)
Right = (N-1)-Left
Count = (Right%(K-1)!=0)+Right//(K-1)
Left -= ((K-1)-Right%(K-1))%(K-1)
Count += (Left%(K-1)!=0)+Left//(K-1)
print(Count)