N=int(input())
B=list(map(int,input().split()))
B=eval(f"[{B[0]}]")+B+eval(f"[{B[N-2]}]")
A=[0]*N
for i in range(N-1):
  A[i]=min(B[i],B[i+1])
A[N-1]=B[N-1]
print(sum(A))
