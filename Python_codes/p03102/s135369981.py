N,M,C = (int(X) for X in input().split())
B = [int(X) for X in input().split()]
Count = 0
for T in range(0,N):
    A = [int(X) for X in input().split()]
    if sum([X*Y for X,Y in zip(A,B)])+C>0:
        Count += 1
print(Count)