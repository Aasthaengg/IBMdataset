N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
print(max(sum(A[N:2*N]),sum(A[1:2*N:2])))