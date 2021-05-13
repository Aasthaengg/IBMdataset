A = sorted([int(X) for X in input().split()],reverse=True)
Cost = [0]+[A[X]-A[X+1] for X in range(0,len(A)-1)]
print(sum(Cost))