N = int(input())
A = list(map(int,input().split()))
AA = [0 for i in range(N)]
 
for i in range(N):
  AA[A[i]-1] = i + 1
  
L=[str(a) for a in AA]
L=" ".join(L)
print(L)