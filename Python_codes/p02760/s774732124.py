A=[list(map(int,input().split())) for _ in range(3)]
b=[i for i in [int(input()) for _ in range(int(input()))] for j in A if i in j]
A=[[0 if A[i][j] in b else A[i][j] for j in range(len(A[i]))] for i in range(len(A))]
print('NYoe s'[any([1 if sum(i)==0 else 0 for i in A]) or any([1 if sum(i)==0 else 0 for i in list(zip(*A))]) or not A[0][0]+A[1][1]+A[2][2] or not A[0][2]+A[1][1]+A[2][0]::2])