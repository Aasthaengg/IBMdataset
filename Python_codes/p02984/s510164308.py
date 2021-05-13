N=int(input())
A=list(map(int,input().split()))
whole=sum(A)
x1=whole
for n in range(1,N,2):
    x1-=A[n]*2
answers=[x1]
for n in range(N-1):
    x=2*A[n]-answers[-1]
    answers.append(x)
print(*answers)
