N=int(input())
A=list(map(int,input().split()))
A = [0]+A+[0]
cum = [0]*(N+2)
for i in range(1, N+2):
    cum[i] = cum[i-1] + abs(A[i]-A[i-1])
for i in range(1, N+1):
    print(cum[N+1]-abs(A[i]-A[i-1])-abs(A[i]-A[i+1])+abs(A[i-1]-A[i+1]))