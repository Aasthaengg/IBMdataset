N, T = map(int, input().split())
A = sorted([list(map(int,input().split())) for n in range(N)])

count=0
for i in range(N):
    count=count+A[i][1]
    if count>=T:
        print(A[i][0])
        exit()