A,B,K = map(int,input().split())
L = []
M = []

for n in range(A,min(A+K,B+1)):
  L.append(n)
  
for n in range(max(A,B-K),B+1):
  M.append(n)
  
L = sorted(set(L[:K]+M[-K:]))
  
print(*L,sep="\n")