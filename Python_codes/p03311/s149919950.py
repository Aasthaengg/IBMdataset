N=int(input())
A=[a-i-1 for i,a in enumerate(list(map(int,input().split())))]
A=sorted(A)
b=(A[N//2]+A[N//2-1])//2 if N%2==0 else A[N//2]
print(sum([abs(a-b) for a in A]))