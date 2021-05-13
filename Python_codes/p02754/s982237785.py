N,A,B=list(map(int, input().split()))
S=A+B
print(N//S*A+min(A,N%S))