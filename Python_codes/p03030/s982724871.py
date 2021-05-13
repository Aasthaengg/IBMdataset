N = int(input())
A = [list(input().split()) for _ in range(N)]
A = [(A[i][0],int(A[i][1]),i+1) for i in range(N)]
A = sorted(A,key=lambda x:x[1],reverse=True)
A = sorted(A,key=lambda x:x[0])
for i in range(N):
    print(A[i][2])