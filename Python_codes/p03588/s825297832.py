N=int(input())
A=[0]*N
B=[0]*N
for i in range(N):
  A[i],B[i] = map(int,input().split())
  
A_max=max(A)
B_min=min(B) 
print(A_max + B_min)