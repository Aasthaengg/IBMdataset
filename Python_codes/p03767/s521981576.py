N = int(input())
A = list(map(int,input().split()))
A=sorted(A,reverse=1)
print(sum(A[1:N*2:2]))