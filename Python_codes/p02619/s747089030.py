D=int(input())
C=list(map(int,input().split()))
S=[list(map(int,input().split())) for i in range(D)]
T=[int(input()) for i in range(D)]
l=[0]*26
v=0
for d in range(D):
    x=[S[d][i]-sum([(d+1-l[j])*C[j] for j in range(26) if i!=j]) for i in range(26)]
    l[T[d]-1]=d+1
    v+=x[T[d]-1]
    print(v)